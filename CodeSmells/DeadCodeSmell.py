import unittest


def my_function(activated):
    return_value = "NOT FOUND"

    if activated:
        return_value = "Live code"

        # I added some comment here just to say I commented the code below in case
        # related_value_i_dont_need_anymore
        # if len(return_value) == 0:
        #   return_value = "Default value"

        if not activated:
            check_version = return_value.lower()

    return return_value


class TestDeadCode(unittest.TestCase):
    def test_should_return_the_correct_value_when_function_is_called(self):
        actual = my_function(True)

        self.assertEqual(actual, "Live code")

if __name__ == "__main__":
    unittest.main()