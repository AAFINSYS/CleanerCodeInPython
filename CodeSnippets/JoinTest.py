import unittest

class TestJoin(unittest.TestCase):
    def test_should_return_a_single_string_of_words_separated_by_underscores_when_join_is_used_on_a_string_list(self):
        input_list = ["My", "name", "is", "Bond", "James", "Bond"]
        actual = "_".join(input_list)

        self.assertEqual(actual, "My_name_is_Bond_James_Bond")

if __name__ == "__main__":
    unittest.main()