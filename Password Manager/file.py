class WorkFile:
    def __init__(self):
        self.hello = "world"

    def append_text(self, website, email, password):
        with open("data.txt", "a") as docs:
            docs.write(f"{website} | {email} | {password}\n")
            docs.close()

    def check_empty(self, website, email, password):
        if len(website) > 0 and len(email) > 0 and len(password) > 0:
            return True
        else:
            return False
