import unittest


def get_a_string():
    return "what you see is what you get"


class Test_FirstClass(unittest.TestCase):
    def test_shouldAssert_When_InputStringIsComparedToTheTargetString(self):
        actual = get_a_string()

        self.assertEqual(actual, "This is not what I will get")


if __name__ == "__main__":
    unittest.main()
