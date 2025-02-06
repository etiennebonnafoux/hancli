import json
from pathlib import Path
from typing import Dict

class Config:
    DEFAULT_COLORS = {
        "title": "blue",
        "score": "green",
        "author": "yellow"
    }
    
    def __init__(self):
        self.config_path = Path.home() / ".hancli"
        self.colors = self.load_config()
    
    def load_config(self) -> Dict[str, str]:
        if not self.config_path.exists():
            self.save_default_config()
            return self.DEFAULT_COLORS
            
        with open(self.config_path, "r") as f:
            return json.load(f)
    
    def save_default_config(self):
        with open(self.config_path, "w") as f:
            json.dump(self.DEFAULT_COLORS, f, indent=2)
