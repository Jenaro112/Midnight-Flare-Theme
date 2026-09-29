import os
import json
import re

file_path = os.path.expanduser("~/Library/Application Support/Code/User/settings.json")

with open(file_path, "r") as f:
    content = f.read()

# Using regex to replace workbench.iconTheme
content = re.sub(r'"workbench.iconTheme":\s*"[^"]+"', '"workbench.iconTheme": "material-icon-theme"', content)

# Remove any existing explorer settings to avoid duplicates (optional, but let's just append)
# Find the last closing brace
last_brace_index = content.rfind("}")

new_config = """
  "workbench.tree.indent": 16,
  "workbench.tree.renderIndentGuides": "always",
  "explorer.compactFolders": true,
  "files.exclude": {
    "**/.git": true,
    "**/.DS_Store": true,
    "**/bin": true,
    "**/obj": true,
    "**/.local": true
  }
"""

before_brace = content[:last_brace_index].strip()
if before_brace.endswith(","):
    insert_str = new_config
else:
    insert_str = ",\n" + new_config

content = content[:last_brace_index][:len(content[:last_brace_index].rstrip())] + "," * (not before_brace.endswith(",")) + "\n" + new_config + "\n}\n"

with open(file_path, "w") as f:
    f.write(content)
