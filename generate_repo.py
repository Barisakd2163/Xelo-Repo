import os, json, re

repo_owner = "Barisakd2163"
repo_name = "Xelo-Repo"
base_url = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/builds"
github_repo = f"https://github.com/{repo_owner}/{repo_name}"
valid_tv_types = {"Movie","TvSeries","Anime","AnimeMovie","OVA","Cartoon","Documentary","Live","NSFW","Others","AsianDrama","Torrent"}

plugins = []
for item in sorted(os.listdir('.')):
    if os.path.isdir(item) and not item.startswith('.') and not item.startswith('__') and item != 'gradle':
        gradle_file = os.path.join(item, 'build.gradle.kts')
        if os.path.isfile(gradle_file):
            with open(gradle_file, 'r', encoding='utf-8') as f:
                txt = f.read()
            v_match = re.search(r'version\s*=\s*(\d+)', txt)
            version = max(1, int(v_match.group(1))) if v_match else 1
            d_match = re.search(r'description\s*=\s*"(.*?)"', txt)
            desc = d_match.group(1) if d_match else f"{item} Plugin"
            l_match = re.search(r'language\s*=\s*"(.*?)"', txt)
            lang = l_match.group(1) if l_match else "tr"
            if lang not in {"tr","en","es","de","fr","it","pt","ru","ja","ko","zh","ar","nl","pl","sv","no","da","fi","cs","sk","hu","ro","bg","hr","sr","uk","el","he","fa","hi","th","vi","id","ms","tl","un"}:
                lang = "un"
            tv_match = re.search(r'tvTypes\s*=\s*listOf\((.*?)\)', txt)
            if tv_match:
                raw = [t.strip().strip('"').strip("'") for t in tv_match.group(1).split(',') if t.strip()]
                clean_types = [t if t in valid_tv_types else "Others" for t in raw] or ["Others"]
            else:
                clean_types = ["Movie","TvSeries"]
            i_match = re.search(r'iconUrl\s*=\s*"(.*?)"', txt)
            icon = i_match.group(1) if i_match else ""
            a_match = re.search(r'authors\s*=\s*listOf\((.*?)\)', txt)
            authors = [a.strip().strip('"').strip("'") for a in a_match.group(1).split(',') if a.strip()] if a_match else ["xelo"]
            s_match = re.search(r'status\s*=\s*(\d+)', txt)
            status = int(s_match.group(1)) if s_match else 1
            
            # Match EXACT Kekik format that works
            plugin_data = {
                "iconUrl": icon,
                "apiVersion": 1,
                "repositoryUrl": github_repo,
                "fileSize": 25000,
                "status": status,
                "language": lang,
                "authors": authors,
                "tvTypes": clean_types,
                "version": version,
                "internalName": item,
                "description": desc,
                "url": f"{base_url}/{item}.cs3",
                "name": item
            }
            plugins.append(plugin_data)

with open('plugins.json', 'w', encoding='utf-8') as f:
    json.dump(plugins, f, indent=4, ensure_ascii=False)
print(f"Generated {len(plugins)} plugins in Kekik-exact format.")
