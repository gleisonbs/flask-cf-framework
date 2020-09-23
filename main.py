from request_handler import RequestHandler
from resources.hello import Hello
from resources.user import User

rh = RequestHandler()
rh.add(Hello, '/hello')
rh.add(User, '/user')

import sys

def main(request):
    return rh.handle(request)

r = {
    # 'method': 'GET',
    'method': sys.argv[1],
    # 'endpoint': '/user',
    'endpoint': sys.argv[2],
    'header': '<>HEADERS</>',
    'body': '<>BODY</>',
    'parameters': '<>PARAMETERS</>'
}

print(main(r))
# 1249873091:AAEvsC4UX4U9ziYvPOrjw4u6gzl7mrWFnLA