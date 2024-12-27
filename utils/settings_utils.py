import json
import os

SETTINGS_FILE = "settings.json"

def load_settings():
    """Load settings from settings.json."""
    if not os.path.exists(SETTINGS_FILE):
        return {"last_folder": ""}
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    """Save settings to settings.json."""
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)