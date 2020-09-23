import unittest
from resources.endpoint import Endpoint
from resources.user import User
from resources.hello import Hello

request = {
    'method': 'GET',
    'endpoint': '/user',
    'header': '<>HEADERS</>',
    'body': '<>BODY</>',
    'parameters': 'Test Parameters'
}

class TestUser(unittest.TestCase):
    def test_get(self):        
        user = User(request)
        self.assertEqual(user.get(), "User -> GET -> Test Parameters") 
        