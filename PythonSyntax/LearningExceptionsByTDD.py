import unittest


def array_access():
    my_array = [0, 1, 2, 3]

    return my_array[100]


def index_exception_safe_array_access():
    try:
        my_array = [0, 1, 2, 3]

        return  my_array[100]
    except IndexError:
        return None


def weird_exception_safe_array_access():
    try:
        my_array = [0, 1, 2, 3]

        return  my_array[100]
    except IndexError:
        raise TimeoutError


def multiple_exception_safe_array_access(a, b):
    try:
        my_array = [0, 1, 2, 3]

        index = int(a / b)

        return my_array[index]
    except (IndexError, ZeroDivisionError) as current_exception:
        return str(current_exception)


def always_raising_exception_array_access(index):
    try:
        my_array = [0, 1, 2, 3]

        return my_array[index]
    except IndexError as current_exception:
        raise RuntimeError
    finally:
        raise RuntimeError

def misleading_exception_array_access(a, b):
    try:
        my_array = [0, 1, 2, 3]

        index = int(a / b)

        return my_array[index]
    except IndexError:
        raise ZeroDivisionError
    except ZeroDivisionError:
        raise IndexError


class TestExceptions(unittest.TestCase):
    def test_should_raise_an_index_error_when_access_for_an_array_out_of_its_bounds(self):
        self.assertRaises(IndexError, array_access)

    def test_should_catch_an_index_error_and_return_None_when_access_for_an_array_out_of_its_bounds(self):
        actual = index_exception_safe_array_access()

        self.assertEqual(actual, None)

    def test_should_raise_an_exception_and_return_None_when_access_for_an_array_out_of_its_bounds(self):
        self.assertRaises(TimeoutError, weird_exception_safe_array_access)

    def test_should_catch_several_exception_types_when_access_for_an_array_out_of_its_bounds(self):
        self.assertEqual('list index out of range', multiple_exception_safe_array_access(10, 1))

        self.assertEqual('division by zero', multiple_exception_safe_array_access(10, 0))

    def test_should_raise_exception_in_any_case_when_an_exception_is_caught(self):
        self.assertRaises(RuntimeError, always_raising_exception_array_access,10)
        self.assertRaises(RuntimeError, always_raising_exception_array_access,0)

    def test_should_not_raise_the_correct_exception_when_IndexError_orZeroDivisionError_are_raised(self):
        self.assertRaises(ZeroDivisionError, misleading_exception_array_access, 10, 1)
        self.assertRaises(IndexError, misleading_exception_array_access,10, 0)


if __name__ == "__main__":
    unittest.main()