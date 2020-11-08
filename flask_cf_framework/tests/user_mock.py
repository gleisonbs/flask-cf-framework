from flask_cf_framework.endpoint import Endpoint


class UserMock(Endpoint):
    def __init__(self, request):
        super().__init__(request)

    def get(self):
        return 'User -> GET', 200

    def delete(self):
        return 'User -> DELETE', 204

    def post(self):
        return 'User -> POST', 201
