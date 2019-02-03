import unittest


def my_own_function(param, param1, param2, param3):
    return param2


def my_own_function_for_named_arg_test(first_named_arguments, second_named_argument, target_named_arguement):
    return target_named_arguement


def my_own_function_with_undefined_number_of_positional_arguments(param, *undefined_nb_of_parameters):
    param_list = []

    for param in undefined_nb_of_parameters:
        param_list.append(param)

    return param_list[-3:]


def my_own_function_with_undefined_number_of_named_arguments(name1, **list_of_named_arguments):
    return list_of_named_arguments["sister"]


class Test_FunctionsAndArguments(unittest.TestCase):
    def test_should_return_third_argument_when_function_is_passed_with_positional_arguments(self):
        actual = my_own_function(1)

        self.assertEqual(actual, "third argument")

    def test_should_return_chosen_named_argument_when_function_is_passed_with_named_argument(self):
        actual = my_own_function_for_named_arg_test("not that one")

        self.assertEqual(actual, "looked for value")

    def test_should_return_the_last_three_positional_arguments_when_a_function_is_passed_six_arguments(self):
        actual = my_own_function_with_undefined_number_of_positional_arguments("John")

        self.assertListEqual(actual, [4, 5, "end"])

    def test_should_return_sister_named_argument_value_when_a_function__is_called_with__six_arguments(self):
        actual = my_own_function_with_undefined_number_of_named_arguments(0, brother1="John", brother2="Dan",
                                                                          number1=4, number2=5,
                                                                          last_argument="end")

        self.assertEqual(actual, "Norma")


def my_own_function_that_return_two_return_values():
    return 5, ["France", "Germany"]


class Test_FunctionAndReturnValues(unittest.TestCase):
    def test_should_return_two_return_values_when_function_is_called(self):
        my_own_function_that_return_two_return_values()

        self.assertEqual(first_return_value, 5)
        self.assertListEqual(second_return_value, ["France", "Germany"])


def outterfunction(innerfunc):
    return innerfunc()


def innerfunction():
    return "return from inner function"


def returnfunction():
    return "return value from returned Function"


def functionreturningafunction():
    return returnfunction


class TestPassingAndReturningFunction(unittest.TestCase):
    def test_should_return_the_result_from_a_function_when_that_function_is_passed_as_argument_to_another_function(
            self):
        outterfunction(innerfunction)

        self.assertEqual(actual, "return from inner function")

    def test_should_return_value_from_a_function_returned_from_a_function_when_a_function_returns_a_function(self):
        return_function = functionreturningafunction()

        return_function()

        self.assertEqual(actual, "return value from returned Function")


if __name__ == "__main__":
    unittest.main()