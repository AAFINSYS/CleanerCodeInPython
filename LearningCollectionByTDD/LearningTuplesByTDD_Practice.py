import unittest


class TestTuples(unittest.TestCase):
    def test_should_return_third_element_of_a_tuple_when_a_tuple_of_four_elements_is_in_input(self):
        current_tuple = (1, 4, "third value of the tuple")

        actual = 2

        self.assertEqual(actual, "third value of the tuple")

    def test_should_return_distinct_variables_from_the_values_of_a_tuple_when_unpacking_a_tuple(self):
        input_tuple = ("first value", "second value", "third value")

        actual1 = 1
        actual2 = 1
        actual3 = 1

        self.assertEqual(actual1, "first value")
        self.assertEqual(actual2, "second value")
        self.assertEqual(actual3, "third value")

    def test_should_unpack_a_tuple_and_throw_away_the_first_value_when_unpacking_a_tuple(self):
        input_tuple = ("first value", "second value", "third value")

        _ = "..."
        actual2 = 2
        actual3 = 5

        self.assertEqual(_, "first value")
        self.assertEqual(actual2, "second value")
        self.assertEqual(actual3, "third value")

    def test_should_unpack_first_and_last_andthrow_away_other_values_when_unpacking_from_a_tuple(self):
        input_tuple = "France", "Italy", "Spain", "Great Britain", "Russia"

        first_value = 3
        _ = [1, 2, 3]
        last_value = 3

        self.assertEqual(first_value, "France")
        self.assertEqual(last_value, "Russia")
        self.assertListEqual(_, ["Italy", "Spain", "Great Britain"])

if __name__ == "__main__":
    unittest.main()