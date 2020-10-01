from flask_cf_framework.endpoint import Endpoint


class User(Endpoint):
    def __init__(self, request):
        super().__init__(request)

    def get(self):
        return 'User -> GET'

    def post(self):
        return 'User -> POST'

    def delete(self):
        return 'User -> DELETE'
