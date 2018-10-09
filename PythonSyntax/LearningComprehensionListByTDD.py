import unittest

class Test_LearningComprehensionListByTDD(unittest.TestCase):
    def test_shouldReturnListOfIntergersUpToTen_When_UsingComprensionListOnARange(self):
        actual = [x for x in range(11)]

        self.assertListEqual(actual, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_shouldReturnListWhenItemsAreDoubled_When_InitialListOfFirstTenFigures(self):
        actual = [2 * x for x in range(10)]

        self.assertListEqual(actual, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

    def test_shouldReturnListOfEvenItems_When_InitialListOfTenFirstFiguresIsProcessed(self):
        actual = [x for x in range(10) if x % 2 == 0]

        self.assertListEqual(actual, [0, 2, 4, 6, 8])



if __name__ == "__main__":
    unittest.main()