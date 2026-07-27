import json
import os


class KeyDatabase:

    def __init__(self):
        self.file = "database/car_keys.json"


    def load(self):

        if not os.path.exists(self.file):
            return []

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)


    def search(self, text):

        data = self.load()

        result = []

        for item in data:

            value = (
                item["brand"]
                + " "
                + item["model"]
            ).lower()

            if text.lower() in value:
                result.append(item)

        return result