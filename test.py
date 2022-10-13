import unittest
from main import area_of_triangle


class TestArea(unittest.TestCase):

    def test_are(self):
        self.assertEqual(area_of_triangle(10, 2), 10)
        self.assertEqual(area_of_triangle(5, 2), 5)
        self.assertEqual(area_of_triangle(10, 4), 20)
        self.assertEqual(area_of_triangle(10, 1), 6)

