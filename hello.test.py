import unittest
from hello import application

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = application.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello World!', response.data)

    def test_other(self):
        tester = application.test_client(self)
        response = tester.get('some-page', content_type='html/text')
        self.assertEqual(response.status_code, 404)
        self.assertTrue(b'does not exist' in response.data)

if __name__ == '__main__':
    unittest.main()
