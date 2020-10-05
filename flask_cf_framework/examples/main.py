from request_handler import RequestHandler
from examples.user import User

rh = RequestHandler()
rh.add(User, '/user')

def main(request):
    return rh.handle(request)