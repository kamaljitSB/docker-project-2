import requests

class Authenticate():
    "stores a dictionary of the user and password"
    def __init__(self):
        self.username = 'admin'
        self.password = 'password'

    def check_credentials(self, username, password):
        "see if user is registered/exists"
        try:
            if username == self.username:
                if password == self.password:
                    print("success")
                    return True
            else:
                raise requests.ConnectionError
        
        except requests.ConnectionError:
            exit()