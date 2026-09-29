import os
import re

file_path = os.path.expanduser("~/Library/Application Support/Code/User/settings.json")

with open(file_path, "r") as f:
    content = f.read()

# Find the last closing brace
last_brace_index = content.rfind("}")

new_config = """
  "better-comments.tags": [
    {
      "tag": "!",
      "color": "#FF2D00",
      "strikethrough": false,
      "underline": false,
      "backgroundColor": "transparent",
      "bold": false,
      "italic": false
    },
    {
      "tag": "?",
      "color": "#00E6C3",
      "strikethrough": false,
      "underline": false,
      "backgroundColor": "transparent",
      "bold": false,
      "italic": false
    },
    {
      "tag": "//",
      "color": "#6C6C86",
      "strikethrough": true,
      "underline": false,
      "backgroundColor": "transparent",
      "bold": false,
      "italic": true
    },
    {
      "tag": "todo",
      "color": "#FF8A00",
      "strikethrough": false,
      "underline": false,
      "backgroundColor": "transparent",
      "bold": true,
      "italic": false
    },
    {
      "tag": "*",
      "color": "#A6E22E",
      "strikethrough": false,
      "underline": false,
      "backgroundColor": "transparent",
      "bold": true,
      "italic": false
    }
  ]
"""

before_brace = content[:last_brace_index].strip()
if before_brace.endswith(","):
    insert_str = new_config
else:
    insert_str = ",\n" + new_config

content = content[:last_brace_index][:len(content[:last_brace_index].rstrip())] + "," * (not before_brace.endswith(",")) + "\n" + new_config + "\n}\n"

with open(file_path, "w") as f:
    f.write(content)
