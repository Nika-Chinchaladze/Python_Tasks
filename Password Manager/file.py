import json


class WorkFile:
    def __init__(self):
        self.hello = "world"

    def create_append_text(self, website, email, password):
        dictionary = {
            website: {
                "email": email,
                "password": password
            }
        }
        with open("data.json", "w") as docs:
            json.dump(dictionary, docs, indent=4)
            docs.close()

    def update_json(self, website, email, password):
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }
        try:
            with open("data.json", "r") as docs:
                output = json.load(docs)
                output.update(new_data)
                docs.close()
        except json.decoder.JSONDecodeError:
            self.create_append_text(website, email, password)
        else:
            with open("data.json", "w") as docs:
                json.dump(output, docs, indent=4)
                docs.close()

    def read_json(self, website):
        with open("data.json", "r") as docs:
            output = json.load(docs)
            docs.close()
            return output[website]

    def just_create_json(self):
        with open("data.json", "w") as docs:
            docs.close()

    def check_empty(self, website, email, password):
        if len(website) > 0 and len(email) > 0 and len(password) > 0:
            return True
        else:
            return False
