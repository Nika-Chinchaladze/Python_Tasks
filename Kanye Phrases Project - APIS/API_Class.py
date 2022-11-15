import requests


class ImportKanye:
    def __init__(self):
        self.api = "https://api.kanye.rest/"

    def get_phrases(self):
        response = requests.get(url=self.api)
        response.raise_for_status()
        data = response.json()
        return data["quote"]

