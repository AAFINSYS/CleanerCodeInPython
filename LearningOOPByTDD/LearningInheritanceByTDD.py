import unittest


class DaughterClass(object):
    LastCalledMethod = ""

    def NotSoAmbiguousMethod(self):
        DaughterClass.LastCalledMethod = "Class Method"

    @classmethod
    def NotSoAmbiguousMethod(cls):
        cls.LastCalledMethod = "Class Method"


class Test_LearningInheritanceByTDD(unittest.TestCase):
    def test_shouldCallInstanceMethod_When_TwoMethodsWithTheSameNameAreDeclaredAtMethodAndClassLevel(self):
        daughter = DaughterClass()

        daughter.NotSoAmbiguousMethod()

        actual = daughter.LastCalledMethod

        self.assertEqual(actual, "Class Method")

if __name__ == "__main__":
    unittest.main()