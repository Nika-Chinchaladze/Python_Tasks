import requests


class Post:
    def __init__(self):
        self.my_api = "https://api.npoint.io/3bb8308bd15e8ff327ef"

    def get_info(self):
        respond = requests.get(url=self.my_api)
        data = respond.json()
        return data
