import unittest
import copy


class SimpleClass(object):
    def __init__(self, numeric_field):
        self.instance_numeric_field = numeric_field


class ClassWithClassProperties(object):
    class_numeric_field = 15

    def __init__(self):
        pass


class ClassToCopy(object):
    def __init__(self, my_array, external_id):
        self.instanceArray = my_array
        self.external_id = external_id


class ClassToCopyWithCustomShallowCopy(object):
    def __init__(self, my_array, external_id):
        self.instanceArray = my_array
        self.external_id = external_id

    def __copy__(self):
        return ClassToCopyWithCustomShallowCopy(self.instanceArray, external_id=self.external_id+1)


class ClassToCopyWithCustomDeepCopy(object):
    def __init__(self, my_array, external_id):
        self.instanceArray = my_array
        self.external_id = external_id

    def __deepcopy__(self, memodict={}):
        return ClassToCopyWithCustomShallowCopy(copy.deepcopy(self.instanceArray), external_id=self.external_id+1)


class ClassWithCustomDel(object):
    classMessage = "No Destruction yet"

    def __del__(self):
        ClassWithCustomDel.classMessage = "Deleted"

class TestClassesAndObjects(unittest.TestCase):
    def setUp(self):
        ClassWithCustomDel.classMessage = "No Destruction yet"

    def test_should_return_instance_value_when_object_is_initialized_in_constructor(self):
        actual = SimpleClass(12)

        self.assertEqual(actual.instance_numeric_field, 12)

    def test_should_return_same_class_value_access_through_two_instances_when_two_instances_are_created(self):
        actual1 = ClassWithClassProperties()
        actual2 = ClassWithClassProperties()

        self.assertEqual(actual1.class_numeric_field, actual2.class_numeric_field)

    def test_should_return_shallow_copy_of_an_object_when_an_object_with_an_array_attribute_is_shallow_copied(self):
        original_instance = ClassToCopy([0, 1, 2, 3], 1)
        cloned_instance = copy.copy(original_instance)

        original_instance.instanceArray[0] = 5

        cloned_instance.external_id = 2

        self.assertListEqual(original_instance.instanceArray, cloned_instance.instanceArray)
        self.assertEqual(id(original_instance.instanceArray), id(cloned_instance.instanceArray))

        self.assertNotEqual(original_instance.external_id, cloned_instance.external_id)

        self.assertNotEqual(id(original_instance), id(cloned_instance))

    def test_should_return_deep_copy_of_an_object_when_an_object_with_an_array_attribute_is_deep_copied(self):
        original_instance = ClassToCopy([0, 1, 2, 3], 1)
        cloned_instance = copy.deepcopy(original_instance)

        original_instance.instanceArray.append(5)

        cloned_instance.external_id = 2

        self.assertNotEqual(len(original_instance.instanceArray), len(cloned_instance.instanceArray))

        self.assertNotEqual(id(original_instance.instanceArray), id(cloned_instance.instanceArray))

        self.assertNotEqual(original_instance.external_id, cloned_instance.external_id)

        self.assertNotEqual(id(original_instance), id(cloned_instance))

    def test_should_return_shallow_copy_of_an_object_when_an_object_with_an_array_attribute_is_customed_shallow_copied(self):
        original_instance = ClassToCopyWithCustomShallowCopy([0, 1, 2, 3], 1)
        cloned_instance = copy.copy(original_instance)

        original_instance.instanceArray[0] = 5

        self.assertListEqual(original_instance.instanceArray, cloned_instance.instanceArray)
        self.assertEqual(id(original_instance.instanceArray), id(cloned_instance.instanceArray))

        self.assertNotEqual(original_instance.external_id, cloned_instance.external_id)

        self.assertNotEqual(id(original_instance), id(cloned_instance))

    def test_should_return_deep_copy_of_an_object_when_an_object_with_an_array_attribute_is_customed_deep_copied(self):
        original_instance = ClassToCopyWithCustomDeepCopy([0, 1, 2, 3], 1)
        cloned_instance = copy.deepcopy(original_instance)

        original_instance.instanceArray.append(5)

        cloned_instance.external_id = 2

        self.assertNotEqual(len(original_instance.instanceArray), len(cloned_instance.instanceArray))

        self.assertNotEqual(id(original_instance.instanceArray), id(cloned_instance.instanceArray))

        self.assertNotEqual(original_instance.external_id, cloned_instance.external_id)

        self.assertNotEqual(id(original_instance), id(cloned_instance))

    def test_should_alter_Class_information_when_an_instance_is_deleted(self):
        self.assertEqual(ClassWithCustomDel.classMessage, "No Destruction yet")

        actual = ClassWithCustomDel()

        del actual

        self.assertEqual(ClassWithCustomDel.classMessage, "Deleted")

    def test_should_alter_Class_information_when_an_instance_goes_out_of_scope(self):
        self.assertEqual(ClassWithCustomDel.classMessage, "No Destruction yet")

        self.instanciateClass()

        self.assertEqual(ClassWithCustomDel.classMessage, "Deleted")

    def instanciateClass(self):
        actual = ClassWithCustomDel()


if __name__ == "__main__":
    unittest.main()