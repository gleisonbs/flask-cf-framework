from resources.endpoint import Endpoint

class Hello(Endpoint):
    def __init__(self, request):
        super().__init__(request)

    def get(self):
        return 'Hello -> GET'

    def post(self):
        return 'Hello -> POST'
