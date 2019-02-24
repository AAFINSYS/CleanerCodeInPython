import unittest


class StrDefinedClass(object):
    def __init__(self, object_id):
        self.id = object_id

    def __str__(self):
        return "instance of class contains {} id value".format(self.id)


class Test__str__MagicMethod(unittest.TestCase):
    def test_should_return_string_representation_of_a_class_instance_when_the_str_function_is_called(self):
        my_instance = StrDefinedClass(12)

        actual = str(my_instance)

        self.assertEqual(actual, "instance of class contains 12 id value")


if __name__ == "__main__":
    unittest.main()