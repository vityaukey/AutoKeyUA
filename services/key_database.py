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
        ) as file:
            return json.load(file)


    def search(self, text):

        keys = self.load()

        result = []

        for item in keys:

            info = (
                item["brand"]
                + " "
                + item["model"]
                + " "
                + item["blade"]
            ).lower()

            if text.lower() in info:
                result.append(item)

        return result