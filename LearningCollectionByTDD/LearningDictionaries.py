import unittest

from collections import defaultdict

class Test_LearningDictionariesByTDD(unittest.TestCase):
    def test_should_return_associated_value_when_key_is_passed_to_dictionary(self):
        country_to_capital_dict = {
            "France": "Paris",
            "Spain": "Madrid",
            "Denmark": "Copenhagen",
            "Italy": "Roma"
        }

        actual = country_to_capital_dict["Denmark"]

        self.assertEqual(actual, "Copenhagen")

    def test_should_return_correct_associated_value_when_key_is_passed_to_an_updated_dictionary(self):
        country_to_capital_dict = {
            "France": "Paris",
            "Spain": "Madrid",
            "Denmark": "Copenhagen",
            "Italy": "Roma",
            "USA": "New York"
        }
        actual = country_to_capital_dict["USA"]

        self.assertEqual(actual, "New York")

        country_to_capital_dict["USA"] = "Washington"
        actual = country_to_capital_dict["USA"]

        self.assertEqual(actual, "Washington")

    def test_should_get_None_value_when_a_missing_key_is_passed_to_a_dictionary(self):
        country_to_capital_dict = {
            "France": "Paris",
            "Spain": "Madrid",
            "Denmark": "Copenhagen",
            "Italy": "Roma",
            "USA": "New York"
        }
        del country_to_capital_dict["USA"]

        actual = country_to_capital_dict.get("USA")

        self.assertEqual(actual, None)

    def test_should_get_Default_value_when_a_missing_key_is_passed_to_a_dictionary(self):
        country_to_capital_dict = {
            "France": "Paris",
            "Spain": "Madrid",
            "Denmark": "Copenhagen",
            "Italy": "Roma",
            "USA": "New York"
        }
        del country_to_capital_dict["USA"]

        actual = country_to_capital_dict.get("USA", "Default Custom Value")

        self.assertEqual(actual, "Default Custom Value")

    def test_should_raise_KeyError_Exception_when_a_missing_key_is_passed_to_a_dictionary(self):
        country_to_capital_dict = {
            "France": "Paris",
            "Spain": "Madrid",
            "Denmark": "Copenhagen",
            "Italy": "Roma",
            "USA": "New York"
        }
        del country_to_capital_dict["USA"]

        self.assertRaises(KeyError, lambda : country_to_capital_dict["USA"])

    def test_should_create_a_dictionary_when_using_a_dict_comprehension_from_a_list_of_tuples(self):
        original_list = [("France", "Paris"), ("Spain", "Madrid"), ("Denmark", "Copenhagen"), ("Italy", "Roma"), ("USA", "New York")]

        actual = {country: capital for (country, capital) in original_list}

        self.assertDictEqual(actual, {
                                        "France": "Paris",
                                        "Spain": "Madrid",
                                        "Denmark": "Copenhagen",
                                        "Italy": "Roma",
                                        "USA": "New York"
                                    })

    def test_should_create_a_dictionary_with_key_a_letter_and_value_thenumber_of_occurrences_in_a_word(self):
        input_string = "Supercalifragilisticexpialidocious"

        actual = {}
        for letter in input_string:
            if letter in actual.keys():
                actual[letter] += 1
            else:
                actual[letter] = 1

        self.assertDictEqual(actual, {'a': 3, 'S': 1, 'c': 3, 'd': 1, 'e': 2, 'f': 1, 'g': 1, 'i': 7, 'l': 3, 'o': 2, 'p': 2, 'r': 2, 's': 2, 't': 1, 'u': 2, 'x': 1})

    def test_should_create_a_dictionary_with_key_a_letter_and_value_the_number_of_occurrences_in_a_word_with_a_defaultdict(self):
        input_string = "Supercalifragilisticexpialidocious"

        actual = defaultdict(int)
        for letter in input_string:
            actual[letter] += 1

        self.assertDictEqual(actual, {'a': 3, 'S': 1, 'c': 3, 'd': 1, 'e': 2, 'f': 1, 'g': 1, 'i': 7, 'l': 3, 'o': 2, 'p': 2, 'r': 2, 's': 2, 't': 1, 'u': 2, 'x': 1})


if __name__ == "__main__":
    unittest.main()