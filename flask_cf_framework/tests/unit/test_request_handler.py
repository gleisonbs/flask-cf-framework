import unittest
from flask_cf_framework.tests.request_mock import RequestMock
from flask_cf_framework.tests.user_mock import UserMock
from flask_cf_framework.request_handler import RequestHandler

class TestRequestHandler(unittest.TestCase):
    def setUp(self):
        self.request = RequestMock()

        self.request_handler = RequestHandler(debug=False)
        self.request_handler.add(UserMock, '/user')

    def test_correct_get_request(self):
        response = self.request_handler.handle(self.request)

        self.assertEqual(response[0], "User -> GET")
        self.assertEqual(response[1], 200)
        self.assertEqual(response[2], {'Access-Control-Allow-Origin': '*'})
        
    def test_invalid_method(self):
        """
        Testing that a request to a not implemented path will return 405
        """
        self.request.method = 'PUT'
        response = self.request_handler.handle(self.request)

        self.assertEqual(response[0], "")
        self.assertEqual(response[1], 405)
        self.assertEqual(response[2], {'Access-Control-Allow-Origin': '*'})

    def test_unhandled_path(self):
        """
        Testing that a request to an unhandled path will return 404
        """
        self.request.path = '/news'
        response = self.request_handler.handle(self.request)

        self.assertEqual(response[0], "")
        self.assertEqual(response[1], 404)
        # self.assertEqual(response[2], {'Access-Control-Allow-Origin': '*'})