from endpoint import Endpoint

class User(Endpoint):
    def __init__(self, request):
        super().__init__(request)
    
    def get(self):
        return 'User -> GET'
    
    def delete(self):
        return 'User -> DELETE'
    
    def post(self):
        return 'User -> POST'
    