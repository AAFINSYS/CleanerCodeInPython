import unittest


class FizzBuzz(object):
    specialCasesDict = {
        3: "Fizz",
        5: "Buzz"
    }

    @classmethod
    def process(cls, param):
        result = ""

        result = cls.specialprocess(param, result, 3)
        result = cls.specialprocess(param, result, 5)

        if result == "":
            return str(param)

        return result

    @classmethod
    def specialprocess(cls, param, result, special_number):
        if param % special_number == 0:
            result += cls.specialCasesDict[special_number]
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