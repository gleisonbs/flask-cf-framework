from resources.endpoint import Endpoint

class Hello(Endpoint):
    def __init__(self, request):
        super().__init__(request)

    def get(self):
        print(self.args)
        return 'Hello -> GET'

    def post(self):
        print(self.args)
        print(self.body)
        return 'Hello -> POST'
