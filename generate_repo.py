import os
import json
import re

repo_owner = "Barisakd2163"
repo_name = "Xelo-Repo"
base_url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/builds"
github_repo = f"https://github.com/{repo_owner}/{repo_name}"

plugins = []

for item in sorted(os.listdir('.')):
    if os.path.isdir(item) and not item.startswith('.') and not item.startswith('__') and item != 'gradle':
        gradle_file = os.path.join(item, 'build.gradle.kts')
        if os.path.isfile(gradle_file):
            with open(gradle_file, 'r', encoding='utf-8') as f:
                txt = f.read()
            
            v_match = re.search(r'version\s*=\s*(\d+)', txt)
            version = int(v_match.group(1)) if v_match else 1
            
            d_match = re.search(r'description\s*=\s*"(.*?)"', txt)
            desc = d_match.group(1) if d_match else f"{item} Plugin"
            
            # Set language to "all" so CloudStream shows it unconditionally!
            lang = "all"
            
            tv_match = re.search(r'tvTypes\s*=\s*listOf\((.*?)\)', txt)
            if tv_match:
                types_raw = tv_match.group(1)
                tv_types = [t.strip().strip('"').strip('\'') for t in types_raw.split(',') if t.strip()]
            else:
                tv_types = ["Movie", "TvSeries"]
            
            i_match = re.search(r'iconUrl\s*=\s*"(.*?)"', txt)
            icon = i_match.group(1) if i_match else ""
            
            a_match = re.search(r'authors\s*=\s*listOf\((.*?)\)', txt)
            if a_match:
                auth_raw = a_match.group(1)
                authors = [a.strip().strip('"').strip('\'') for a in auth_raw.split(',') if a.strip()]
            else:
                authors = ["xelo"]

            s_match = re.search(r'status\s*=\s*(\d+)', txt)
            status = int(s_match.group(1)) if s_match else 1
            
            plugin_data = {
                "name": item,
                "internalName": item,
                "version": version,
                "url": f"{base_url}/{item}.cs3",
                "apiVersion": 1,
                "repositoryUrl": github_repo,
                "authors": authors,
                "status": status,
                "language": lang,
                "tvTypes": tv_types,
                "iconUrl": icon,
                "description": desc,
                "fileSize": 25000
            }
            plugins.append(plugin_data)

with open('plugins.json', 'w', encoding='utf-8') as f:
    json.dump(plugins, f, indent=4, ensure_ascii=False)

print(f"Generated plugins.json with {len(plugins)} plugins (language: all).")
