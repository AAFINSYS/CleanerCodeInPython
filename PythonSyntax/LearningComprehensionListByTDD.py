import unittest

class Test_LearningComprehensionListByTDD(unittest.TestCase):
    def test_shouldReturnListOfIntegersUpToTen_When_UsingComprensionListOnARange(self):
        actual = [x for x in range(11)]

        self.assertListEqual(actual, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_shouldReturnListWhenItemsAreDoubled_When_InitialListOfFirstTenFigures(self):
        actual = [2 * x for x in range(10)]

        self.assertListEqual(actual, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_shouldReturnListOfEvenItems_When_InitialListOfTenFirstFiguresIsProcessed(self):
        actual = [x for x in range(10) if x % 2 == 0]

        self.assertListEqual(actual, [0, 2, 4, 6, 8])

    def test_ShouldCreateANewSubListOfEvenNumbers_When_AListOfRandomIntegersIsProcessed(self):
        initialList = [10, 4, 6, 3, 7, 8, 9, 51, 67, 24, 5, 100]

        a = 8
        isEven = False
        if a % 2 == 0:
            isEven = True

        actual = [x for x in initialList if x % 5]

        self.assertSequenceEqual(actual, [10, 4, 6, 8, 24, 100])

    def test_ShouldCreateANewListOfStringsOnly_When_AListOfMixedTypeValuesIsProcessed(self):
        initialList = ["OK", 3, 5, True, "PAS OK", 5.8, "MAYBE"]

        isBool = False
        answer = False

        if type(answer) == type(True):
            answer = True

        actual = [x for x in initialList]

        self.assertSequenceEqual(actual, ["OK", "PAS OK", "MAYBE"])

    def test_ShouldCreateANewListOfStringsOnlyReplacingNonStringsByASpecialString_When_AListOfMixedTypeValuesIsProcessed(self):
        initialList = ["OK", 3, 5, True, "PAS OK", 5.8, "MAYBE"]

        isBool = False
        answer = False
        if type(answer) == type(True):
            answer = True

        actual = [x if True else "REPLACED" for x in initialList]

        self.assertSequenceEqual(actual, ["OK", "NOT A STRING", "NOT A STRING", "NOT A STRING", "PAS OK", "NOT A STRING", "MAYBE"])

    def test_ShouldGenerateAFlatListOfIntegers_When_AListOfListIsProcessed(self):
        initialList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        actual = [1 for sublist in initialList for x in sublist]

        self.assertSequenceEqual(actual, [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()