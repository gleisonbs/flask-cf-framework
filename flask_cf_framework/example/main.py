from flask_cf_framework.request_handler import RequestHandler
from resources.user import User

rh = RequestHandler()
rh.add(User, '/users')


def main(request):
    return rh.handle(request)
