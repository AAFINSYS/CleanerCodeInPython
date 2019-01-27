import unittest


class Test_LearningDictionariesByTDD(unittest.TestCase):
    def test_should_return_associated_value_when_key_is_passed_to_dictionary(self):
        countryToCapitalDict = {
            "France": "Paris",
            "Spain": "Madrid",
            "Denmark": "Copenhagen",
            "Italy": "Roma"
        }

        actual = countryToCapitalDict["Denmark"]

        self.assertEqual(actual, "Copenhagen")

    def test_should_return_correct_associated_value_when_key_is_passed_to_an_updated_dictionary(self):
        countryToCapitalDict = {
            "France": "Paris",
            "Spain": "Madrid",
            "Denmark": "Copenhagen",
            "Italy": "Roma",
            "USA": "New York"
        }
        actual = countryToCapitalDict["USA"]

        self.assertEqual(actual, "New York")

        countryToCapitalDict["USA"] = "Washington"
        actual = countryToCapitalDict["USA"]

        self.assertEqual(actual, "Washington")

    def test_should_get_None_value_when_a_missing_key_is_passed_to_a_dictionary(self):
        countryToCapitalDict = {
            "France": "Paris",
            "Spain": "Madrid",
            "Denmark": "Copenhagen",
            "Italy": "Roma",
            "USA": "New York"
        }
        del countryToCapitalDict["USA"]

        actual = countryToCapitalDict.get("USA")

        self.assertEqual(actual, None)

    def test_should_get_Default_value_when_a_missing_key_is_passed_to_a_dictionary(self):
        countryToCapitalDict = {
            "France": "Paris",
            "Spain": "Madrid",
            "Denmark": "Copenhagen",
            "Italy": "Roma",
            "USA": "New York"
        }
        del countryToCapitalDict["USA"]

        actual = countryToCapitalDict.get("USA", "Default Custom Value")

        self.assertEqual(actual, "Default Custom Value")

    def test_should_raise_KeyError_Exception_when_a_missing_key_is_passed_to_a_dictionary(self):
        countryToCapitalDict = {
            "France": "Paris",
            "Spain": "Madrid",
            "Denmark": "Copenhagen",
            "Italy": "Roma",
            "USA": "New York"
        }
        del countryToCapitalDict["USA"]

        self.assertRaises(KeyError, lambda : countryToCapitalDict["USA"])

    def test_should_create_a_dictionary_when_using_a_dict_comprehension_from_a_list_of_tuples(self):
        originalList = [("France", "Paris"), ("Spain", "Madrid"), ("Denmark", "Copenhagen"), ("Italy", "Roma"), ("USA", "New York")]

        actual = {country: capital for (country, capital) in originalList}

        self.assertDictEqual(actual, {
                                        "France": "Paris",
                                        "Spain": "Madrid",
                                        "Denmark": "Copenhagen",
                                        "Italy": "Roma",
                                        "USA": "New York"
                                    })



if __name__ == "__main__":
    unittest.main()