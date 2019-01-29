import unittest


def manualIteration(param):
    manual_iter = iter(param)

    first_value = manual_iter.__next__()
    second_value = manual_iter.__next__()
    third_value = manual_iter.__next__()
    fourth_value = manual_iter.__next__()
    no_value_here = manual_iter.__next__()


class Test_ManuallyUsingIter(unittest.TestCase):
    def test_should_raise_exception_when_manually_iterating_on_a_list(self):

        self.assertRaises(StopIteration, manualIteration, [2, 3, 5, 6])

if __name__ == "__main__":
    unittest.main()