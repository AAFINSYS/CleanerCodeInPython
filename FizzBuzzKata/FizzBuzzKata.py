import unittest


class FizzBuzz(object):
    specialCasesDict = {
        3: "Fizz",
        5: "Buzz"
    }

    @classmethod
    def Process(cls, param):
        result = ""

        result = cls.SpecialProcess(param, result, 3)
        result = cls.SpecialProcess(param, result, 5)

        if result == "":
            return str(param)

        return result

    @classmethod
    def SpecialProcess(cls, param, result, specialNumber):
        if param % specialNumber == 0:
            result += cls.specialCasesDict[specialNumber]
        return result


class Test_FizzBuzz(unittest.TestCase):
    def test_shouldReurnnumber_When_InputNumberIsRegular(self):
        actual = FizzBuzz.Process(1)

        self.assertEqual(actual, "1")

    def test_shouldReturnFizz_When_inputNumberIsAMultipleOfThree(self):
        actual = FizzBuzz.Process(3)

        self.assertEqual(actual, "Fizz")

    def test_shouldReturnBuzz_When_inputNumberIsAMultipleOfFive(self):
        actual = FizzBuzz.Process(5)

        self.assertEqual(actual, "Buzz")

    def test_shouldReturnFizzBuzz_When_InputNumberIsAMultipleOfThreeAndFive(self):
        actual = FizzBuzz.Process(15)

        self.assertEqual(actual, "FizzBuzz")

if __name__ == "__main__":
    unittest.main()