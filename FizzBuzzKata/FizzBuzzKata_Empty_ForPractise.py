import unittest


class FizzBuzz(object):
    @classmethod
    def process(cls, param):
        result = ""

        return result



class Test_FizzBuzz(unittest.TestCase):
    def test_shouldReurnnumber_When_InputNumberIsRegular(self):
        actual = FizzBuzz.process(1)

        self.assertEqual(actual, "1")

    def test_shouldReturnFizz_When_inputNumberIsAMultipleOfThree(self):
        actual = FizzBuzz.process(3)

        self.assertEqual(actual, "Fizz")

    def test_shouldReturnBuzz_When_inputNumberIsAMultipleOfFive(self):
        actual = FizzBuzz.process(5)

        self.assertEqual(actual, "Buzz")

    def test_shouldReturnFizzBuzz_When_InputNumberIsAMultipleOfThreeAndFive(self):
        actual = FizzBuzz.process(15)

        self.assertEqual(actual, "FizzBuzz")

if __name__ == "__main__":
    unittest.main()