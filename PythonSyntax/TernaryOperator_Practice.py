import unittest

class Test_TestingTernaryOperatorByTDD(unittest.TestCase):
    def test_shouldReturnTrueAssociatedValue_When_TernaryOperator_Is_InvokedWithTrueCondition(self):
        actual = "..." if False else "..."

        self.assertEqual(actual, "First Condition")

    def test_shouldReturnFalseAssociatedValue_When_TernaryOperator_Is_InvokedWithFalseCondition(self):
        actual = "..." if True else "..."

        self.assertEqual(actual, "Second Condition")

if __name__ == "__main__":
    unittest.main()