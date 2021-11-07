class Credentials:
    def __init__(self):
        self._username = None
        self._passwd = None
        self._app_token = None

    def ext(self):
        with open('/home/alev/personalProjects/WebScrapper/project/Acc.txt', 'r') as f:
            data = f.read()
        res = [x.strip() for x in data.split(',')]
        self._username = res[0]
        self._passwd = res[1]
        self._app_token = res[2]
        return self._app_token, self._username, self._passwd
    



# cred = ext()
# data = Credentials()
# data.setUser(cred[0])
# data.setPass(cred[1])
# data.setAppToken(cred[2])
    # u.setUser(list(cred.items())[0][0])
    # u.setPass(list(cred.items())[0][1])
