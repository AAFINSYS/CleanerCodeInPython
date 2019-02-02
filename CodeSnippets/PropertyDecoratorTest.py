import unittest


class ClassicRectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class PropertyRectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_value):
        if new_value <= 0:
            raise ValueError

        self._width = new_value

    @length.setter
    def length(self, new_value):
        if new_value <= 0:
            raise ValueError

        self._length = new_value


def set_property_rectangle_width_to_negative_number(property_rectangle):
    property_rectangle.width = -10


def set_property_rectangle_length_to_negative_number(property_rectangle):
    property_rectangle.length = -40


class TestPropertyDecorator(unittest.TestCase):
    def test_should_return_same_length_and_width_for_two_different_classes_when_using_direct_access_or_property_decorator(self):
        classic_rectangle = ClassicRectangle(10, 20)
        property_rectangle = PropertyRectangle(10, 20)

        self.assertEqual(classic_rectangle.length, property_rectangle.length)
        self.assertEqual(classic_rectangle.width, property_rectangle.width)

    def test_should_raise_exception_when_setting_bad_values_for_PropertyRectangle(self):
        property_rectangle = PropertyRectangle(10, 20)

        self.assertRaises(ValueError, set_property_rectangle_width_to_negative_number, property_rectangle)
        self.assertRaises(ValueError, set_property_rectangle_length_to_negative_number, property_rectangle)


if __name__ == "__main__":
    unittest.main()