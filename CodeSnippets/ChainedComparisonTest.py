import unittest

class TestChainedComparison(unittest.TestCase):
    def test_should_return_correct_comparison_result_when_a_comparison_is_done_with_one_comparison(self):
        actual = False
        base_number = 10

        if 1 < base_number < 100:
            actual = True

        self.assertTrue(actual)

    def test_should_return_correct_comparison_result_when_a_comparison_is_done_with_one_ternary_comparison(self):
        base_number = 10

        actual = True if 1 < base_number < 100 else False

        self.assertTrue(actual)


if __name__ == "__main__":
    unittest.main()
