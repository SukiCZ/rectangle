import unittest

from objects import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_object(self):
        rectangle_1 = Rectangle("0 0 10 10")
        rectangle_2 = Rectangle("5 5 15 15")
        rectangle_3 = Rectangle("1 1 9 9")
        self.assertTrue(rectangle_1.do_overlap(rectangle_2))
        self.assertTrue(rectangle_2.do_overlap(rectangle_1))
        self.assertFalse(rectangle_1.do_overlap(rectangle_3))
        self.assertTrue(rectangle_1.has_inside(rectangle_3))

    def test_initialize_rectangle_with_missing_side(self):
        with self.assertRaises(AssertionError):
            Rectangle("foo bar")

    def test_initialize_rectangle_with_string(self):
        with self.assertRaises(ValueError):
            Rectangle("foo bar fizz buzz")
