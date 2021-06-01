import unittest
import requests

class TestStringMethods(unittest.TestCase):

    API_URL = "http://localhost:8000"
    TOKEN = ''

    @classmethod
    def setUpClass(cls):
        credentials_dict = {"username": "test", "password": "1234"}
        headers = {"Content-Type": "application/json"}
        url = cls.API_URL + "/api/auth"
        response = requests.post(url, data=credentials_dict, headers=headers)

        cls.TOKEN = response.json()
        print(cls.TOKEN)


    def setUp(self) -> None:
        super().setUp()

    def test_foo(self):
        self.assertTrue(1,1)

if __name__ == '__main__':
    unittest.main()


 # post to API auth : 
 # 1. {'error': 'Internal Server Error', 'message': 'Failed when parsing body as json'}
 # 2. Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))