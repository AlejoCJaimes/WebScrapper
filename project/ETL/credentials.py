class Credentials:
    def __init__(self):
        self._username = None
        self._passwd = None
        self._app_token = None

    def setUser(self, username):
        self._username = username

    def setPass(self, passd):
        self._passwd = passd

    def setAppToken(self, app_token):
        self._app_token = app_token

    def getUser(self):
        return self._username

    def getPass(self):
        return self._passwd

    def getToken(self):
        return self._app_token
    username = property(getUser, setUser)
    passwd = property(getPass, setPass)
    app_token = property(getToken, setAppToken)


def ext():
    with open('/home/alev/personalProjects/WebScrapper/project/Acc.txt', 'r') as f:
        data = f.read()
    res = [x.strip() for x in data.split(',')]
    return res



cred = ext()
data = Credentials()
data.setUser(cred[0])
data.setPass(cred[1])
data.setAppToken(cred[2])
    # u.setUser(list(cred.items())[0][0])
    # u.setPass(list(cred.items())[0][1])
