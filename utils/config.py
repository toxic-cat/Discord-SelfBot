import json

class Config:
    def __init__(self, path="config.json"):
        self.path = path
        self.config = self.load_config()

    def load_config(self):
        with open(self.path, "r") as file:
            return json.load(file)

    def save_config(self):
        with open(self.path, "w") as file:
            json.dump(self.config, file, indent=4)

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()
