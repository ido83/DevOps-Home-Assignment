from app.app import hello_devops
import unittest

class TestHello(unittest.TestCase):
    def test_hello_devops(self):
        self.assertIn("Hello", hello_devops(), "all good.")
