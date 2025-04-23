import unittest
from app.app import app

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        
    def test_home_data(self):
        result = self.app.get('/')
        self.assertEqual(result.data.decode('utf-8'), "I like agile software engineering")

if __name__ == '__main__':
    unittest.main()
