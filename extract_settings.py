import os
import json

file_path = os.path.expanduser("~/Library/Application Support/Code/User/settings.json")

# I'll just write the configuration snippet manually since I know exactly what I injected earlier.
# This avoids any parsing issues with trailing commas in their settings.json.
new_config = {
  "better-comments.tags": [
    {
      "tag": "!",
      "color": "#FF2D00",
      "strikethrough": False,
      "underline": False,
      "backgroundColor": "transparent",
      "bold": False,
      "italic": False
    },
    {
      "tag": "?",
      "color": "#00E6C3",
      "strikethrough": False,
      "underline": False,
      "backgroundColor": "transparent",
      "bold": False,
      "italic": False
    },
    {
      "tag": "//",
      "color": "#6C6C86",
      "strikethrough": True,
      "underline": False,
      "backgroundColor": "transparent",
      "bold": False,
      "italic": True
    },
    {
      "tag": "todo",
      "color": "#FF8A00",
      "strikethrough": False,
      "underline": False,
      "backgroundColor": "transparent",
      "bold": True,
      "italic": False
    },
    {
      "tag": "*",
      "color": "#A6E22E",
      "strikethrough": False,
      "underline": False,
      "backgroundColor": "transparent",
      "bold": True,
      "italic": False
    }
  ]
}

with open("better-comments-settings.json", "w") as f:
    json.dump(new_config, f, indent=2)

print("Created better-comments-settings.json")
