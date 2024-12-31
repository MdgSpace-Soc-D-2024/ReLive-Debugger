import unittest
from app.visualizer import app

class TestVisualizer(unittest.TestCase):
    def test_index_page(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Time Travel Debugger', response.data)
