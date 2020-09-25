from request_handler import RequestHandler
from resources.hello import Hello
from resources.user import User

rh = RequestHandler()
rh.add(Hello, '/hello')
rh.add(User, '/user')

def main(request):
    return rh.handle(request)
