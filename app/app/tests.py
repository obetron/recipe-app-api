from django.test import TestCase
from app.calc import add, substract


class MyTestCase(TestCase):
    def test_add(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(11, 3), 14)

    def test_substract(self):
        """Test that values are substracted and returned"""
        self.assertEqual(substract(5, 11), 6)
