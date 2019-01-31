import unittest


class Test_Enumerate(unittest.TestCase):
    def test_should_return_a_list_of_indexes_of_a_list_elements_when_a_list_is_iterated_through_enumerate(self):
        input_list = ["France", "Spain", "Italy", "Denmark", "Russia", "Portugal"]

        actual = []
        for current_index, list_value_at_current_index in enumerate(input_list):
            actual.append(current_index)

        self.assertListEqual(actual, [0, 1, 2, 3, 4, 5])

    def test_should_return_a_list_of_indexes_of_a_list_elements_when_a_list_is_iterated_through_enumerate_in_a_listcomp(self):
        input_list = ["France", "Spain", "Italy", "Denmark", "Russia", "Portugal"]

        actual = [current_index for current_index, list_value_at_current_index in enumerate(input_list)]

        self.assertListEqual(actual, [0, 1, 2, 3, 4, 5])

    def test_should_return_the_input_string_in_camel_case_formatting_when_a_string_is_processed_with_enumerate(self):
        input_string = "My tailor is rich"

        mots = input_string.lower().split(' ')
        actual = mots[0]
        for i, mot in enumerate(mots):
            if i > 0:
                actual += mot.capitalize()

        self.assertEqual(actual, "myTailorIsRich")

if __name__ == "__main__":
        unittest.main()