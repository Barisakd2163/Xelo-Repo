import requests

sites = {
    "Dizipal": "https://dizipal{}.com",
    "DiziYou": "https://diziyou{}.com",
    "Dizilla": "https://dizilla{}.com"
}

for site, url_template in sites.items():
    for i in range(950, 1000):
        url = url_template.format(i)
        if "dizilla" in site.lower(): url = f"https://dizilla{i}.com" # some variation
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                print(f"Found {site}: {url}")
                break
        except:
            pass
