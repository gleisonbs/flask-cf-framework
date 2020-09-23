from resources.endpoint import Endpoint

class User(Endpoint):
    def __init__(self, request):
        super().__init__(request)

    def get(self):
        return f'User -> GET'

    def post(self):
        return 'User -> POST'