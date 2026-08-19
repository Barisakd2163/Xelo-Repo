import os
import re

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.kt'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except: continue
            
            content = re.sub(r'\.toRatingInt\(\)', '', content)
            content = re.sub(r'isM3u8\s*=\s*true', 'type = ExtractorLinkType.M3U8', content)
            content = re.sub(r'isM3u8\s*=\s*false', 'type = ExtractorLinkType.VIDEO', content)
            content = re.sub(r'ExtractorLinkType\.INFER', 'ExtractorLinkType.VIDEO', content)
            content = re.sub(r'override\s+var\s+rating\s*:\s*Int\?\s*=\s*null', '', content)
            content = re.sub(r'var\s+rating\s*:\s*Int\?\s*=\s*null', '', content)
            content = re.sub(r'(\n\s*)(this\.)?rating\s*=', r'\1// rating =', content)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
