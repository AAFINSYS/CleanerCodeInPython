import unittest


class Rectangle(object):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def __repr__(self):
        return "Rectangle(length=%d, width=%d)" % (self.length, self.width)


class Test_repr(unittest.TestCase):
    def test_should_return_repr_string_when_repr_function_is_called(self):
        actual = repr(Rectangle(length=5, width=12))

        self.assertEqual(actual, "Rectangle(length=5, width=12)")


if __name__ == "__main__":
    unittest.main()