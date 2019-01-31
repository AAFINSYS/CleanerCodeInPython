import unittest


class TestTuples(unittest.TestCase):
    def test_should_return_third_element_of_a_tuple_when_a_tuple_of_four_elements_is_retrieved(self):
        current_tuple = (1, 4, "third value of the tuple")

        actual = current_tuple[2]

        self.assertEqual(actual, "third value of the tuple")

    def test_should_return_distinct_variables_from_the_values_of_a_tuple_when_unpacking_a_tuple(self):
        input_tuple = ("first value", "second value", "third value")

        actual1, actual2, actual3 = input_tuple

        self.assertEqual(actual1, "first value")
        self.assertEqual(actual2, "second value")
        self.assertEqual(actual3, "third value")

    def test_should_unpack_a_tuple_and_throw_away_the_first_value_when_unpacking_a_tuple(self):
        input_tuple = ("first value", "second value", "third value")

        _, actual2, actual3 = input_tuple

        self.assertEqual(_, "first value")
        self.assertEqual(actual2, "second value")
        self.assertEqual(actual3, "third value")


if __name__ == "__main__":
    unittest.main()