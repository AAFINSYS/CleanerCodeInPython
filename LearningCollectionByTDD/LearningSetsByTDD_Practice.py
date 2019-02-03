import unittest


class TestSet(unittest.TestCase):
    def test_should_create_Set_when_duplicate_key_is_added(self):
        my_own_set = set()
        my_own_set.add("train")

        my_own_set.add("train")

        actual = 0

        self.assertEqual(actual, 5)

    def test_should_create_a_set_when_a_list_is_in_input(self):
        my_own_set = {"car", "bike", "boat", "train", "car", "bike", "boat", "motorbike", "train"}

        actual = len(my_own_set)

        self.assertEqual(actual, 0)

    def test_should_return_an_intersection_of_sets_whe_two_distinct_sets_are_intersected(self):
        my_first_own_set = {}
        my_second_own_set = {}

        actual = my_first_own_set.intersection(my_second_own_set)

        self.assertEqual(len(actual), 2)

if __name__ == "__main__":
    unittest.main()
