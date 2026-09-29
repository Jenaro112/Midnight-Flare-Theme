import os
import re

file_path = os.path.expanduser("~/Library/Application Support/Code/User/settings.json")

with open(file_path, "r") as f:
    content = f.read()

# Using regex to replace workbench.iconTheme back to symbols
content = re.sub(r'"workbench.iconTheme":\s*"[^"]+"', '"workbench.iconTheme": "symbols"', content)

with open(file_path, "w") as f:
    f.write(content)
