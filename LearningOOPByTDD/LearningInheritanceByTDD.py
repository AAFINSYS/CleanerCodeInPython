import unittest


class BaseClass:
    def __init__(self, input_data=20):
        self.base_class_data = input_data

    def only_in_base_class(self):
        return "only_in_base_class"

    def in_both_classes(self):
        return "only_in_base_class from base class"

    def set_base_class_data(self):
        self.base_class_data = 100


class ChildClass(BaseClass):
    def __init__(self, input_data=200):
        self.child_class_data = input_data

    def in_both_classes(self):
        return "only_in_base_class from child class"


class AnotherChildClass(BaseClass):
    def __init__(self, input_data=200):
        super(AnotherChildClass, self).__init__(50)
        self.child_class_data = input_data

    def in_both_classes(self):
        return "only_in_base_class from child class"


class TestLearningInheritanceByTDD(unittest.TestCase):
    def test_should_call_base_instance_method_when_calling_from_child_class_instance_and_does_not_exist_in_child_class(self):
        child_instance = ChildClass()
        actual = child_instance.only_in_base_class()

        self.assertEqual(actual, "only_in_base_class")

    def test_should_call_child_instance_method_when_function_is_defined_at_base_and_children_level(self):
        child_instance = ChildClass()
        actual = child_instance.in_both_classes()

        self.assertEqual(actual, "only_in_base_class from child class")

    def test_should_get_child_instance_data_when_some_date_is_init_at_children_level(self):
        child_instance = ChildClass()
        child_instance.set_base_class_data()

        self.assertEqual(child_instance.base_class_data, 100)
        self.assertEqual(child_instance.child_class_data, 200)

    def test_should_get_child_instance_data_when_some_date_is_init_at_children_level_and_calls_super(self):
        child_instance = AnotherChildClass()

        self.assertEqual(child_instance.base_class_data, 50)
        self.assertEqual(child_instance.child_class_data, 200)


if __name__ == "__main__":
    unittest.main()