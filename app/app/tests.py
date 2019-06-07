from django.test import TestCase
from app.calc import add

class MyTestCase(TestCase):
    def test_add(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(11, 3), 14)