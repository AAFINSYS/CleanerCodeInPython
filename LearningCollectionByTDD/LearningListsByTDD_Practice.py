import unittest


class Test_LearningListsInTDD(unittest.TestCase):
    def test_shouldReturnZeroSize_When_EmptyListIsAskedForItsLength(self):
        myEmptyList = list()
        actual = len([1])

        self.assertEqual(actual, len(myEmptyList))

    def test_shouldReturnAnUpdatedListWithAnAdditionnalElement_When_AnElementIsInsertedInAList(self):
        actual = [2, 3, 4, 5]

        self.assertListEqual(actual, [1, 2, 3, 4, 5])

    def test_shouldReturnAListOfTheFiveFirstIntegers_When_AnListOfFfFiveZeroIsModified(self):
        actual = [0, 0, 0, 0, 0]

        self.assertListEqual(actual, [1, 2, 3, 4, 5])

    def test_should_ReturnAListOfOnes_When_AlistOfSeveralDifferentIntegersIsInInput(self):
        actual = [2, 1, 1, 3, 2, 1, 1, 9]

        self.assertListEqual(actual, [1, 1, 1, 1])

    def test_shouldReturnAListOfIntegers_When_A_ListContainingIntegersAndAStringAsTheLastElementIsProcessed(self):
        actual = [5, 10, 15, "ToPop"]

        popped_item = ""

        self.assertEqual(popped_item, "ToPop")
        self.assertListEqual(actual, [5, 10, 15])

    def test_shouldRemoveTheThirdElementInAList_When_AListOfSixElementsIsProcessed(self):
        actual = [1, 4, "OK", 7, "KO", 2]

        self.assertListEqual(actual, [1, 4, 7, "KO", 2])

    def test_shouldReturnASubListOfItemsFromTheSecondToTheFifth_When_AListOfTenItemsIsSlicedBetweenTheSecondAndTheFifthItems(self):
        actual = []
        actual.append(1)
        actual.append(2)
        actual.append(3)
        actual.append(4)
        actual.append(5)
        actual.append(6)
        actual.append(7)
        actual.append(8)
        actual.append(9)
        actual.append(10)

        self.assertListEqual(actual, [2, 3, 4])

    def test_shouldReturnFirstThreeItems_When_aListOfSixItemsIsSlicedForItsFirstThreeItems(self):
        actual = list()

        for x in range(6):
            actual.append(x)

        self.assertListEqual(actual, [0, 1, 2])

    def test_shouldReturnLastFourItems_When_AListOfEightItemsIsSlicedForItsFirstFourItems(self):
        actual = [x for x in range(8)]

        self.assertListEqual(actual, [4, 5, 6, 7])

    def test_shouldReturnItemsFromTheSixthToTheEnd_When_AListOfNineItemsIsSlicedFromTheSixth(self):
        actual = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        self.assertListEqual(actual, [5, 6, 7, 8])

    def test_shouldReturnUpdatedListWithSecondAnThirdElementReplacedWithANewList_When_SlicingAndInsertingInAList(self):
        actual = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        self.assertListEqual(actual, [0, 'a', 'b', 'c', 'd', 3, 4, 5, 6, 7, 8])

    def test_shouldReturnEverySecondItem_When_aListIsSlicedWithStrideOptionFromTheBeginning(self):
        actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.assertListEqual(actual, [0, 2, 4, 6, 8])

    def test_shouldReturnEverySecondItemFromTheEnd_When_aListIsSlicedWithStrideOptionFromTheEnd(self):
        actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.assertListEqual(actual, [9, 7, 5, 3, 1])


if __name__ == "__main__":
    unittest.main()