import os
import re

count = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.kt'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # fix dangling ? at end of line (e.g., trim()?)
            new_content = re.sub(r'\?\s*$', '', content, flags=re.MULTILINE)
            # fix dangling ?. at end of line
            new_content = re.sub(r'\?\.\s*$', '', new_content, flags=re.MULTILINE)
            # fix unused rating lines if they cause warnings/errors
            # also replace any remaining .toRatingInt() or toRatingInt()
            new_content = re.sub(r'\??\.toRatingInt\(\)', '', new_content)
            
            if new_content != content:
                count += 1
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

print(f"Fixed {count} files")
