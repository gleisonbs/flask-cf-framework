import unittest
from resources.endpoint import Endpoint
from resources.user import User
from resources.hello import Hello

class Request:
    def __init__(self):
        self.method = 'GET',
        self.endpoint = '/user',
        self.headers = '<>HEADERS</>',
        self.body = '<>BODY</>',
        self.args = 'Test Parameters'

    def get_json(self, silent=False):
        return self.body

class TestUser(unittest.TestCase):
    def test_get(self):        
        user = User(Request())
        self.assertEqual(user.get(), "User -> GET") 
        