class RequestMock:
    def __init__(self):
        self.method = 'GET'
        self.path = '/user'
        self.headers = '<>HEADERS</>'
        self.body = '<>BODY</>'
        self.args = 'Test Parameters'

    def get_json(self, silent=False):
        return self.body