import json, re, os

# Download Kekik plugins.json as template
import urllib.request
url = "https://raw.githubusercontent.com/keyiflerolsun/Kekik-cloudstream/builds/plugins.json"
with urllib.request.urlopen(url) as r:
    kekik = json.loads(r.read().decode())

# Our builds cs3 files list - exact filenames
builds_url = "https://raw.githubusercontent.com/Barisakd2163/Xelo-Repo/builds"
our_repo = "https://github.com/Barisakd2163/Xelo-Repo"

# Get our actual cs3 files from builds branch
cs3_url = "https://api.github.com/repos/Barisakd2163/Xelo-Repo/contents/?ref=builds"
with urllib.request.urlopen(cs3_url) as r:
    contents = json.loads(r.read().decode())

cs3_files = {item["name"].replace(".cs3","") for item in contents if item["name"].endswith(".cs3")}
print(f"CS3 files in builds: {sorted(cs3_files)}")

# Filter Kekik plugins to ones we have + fix URLs
our_plugins = []
for p in kekik:
    name = p["name"]
    if name in cs3_files:
        new_p = dict(p)
        new_p["url"] = f"{builds_url}/{name}.cs3"
        new_p["repositoryUrl"] = our_repo
        our_plugins.append(new_p)

print(f"\nMatching plugins: {len(our_plugins)}")
for p in our_plugins:
    print(f"  {p['name']}")

with open("plugins.json", "w", encoding="utf-8") as f:
    json.dump(our_plugins, f, indent=4, ensure_ascii=False)
print("\nDone!")
