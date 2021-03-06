import unittest
import sys


class Algorithm:

    def template_method(self):
        """Generic pattern of operations to perform. DO NOT override.
        """
        result0 = self.__private_method()
        result1 = self.specific_processing_1()
        result2 = self.specific_processing_2()
        result3 = self.common_processings()

        return result0 + result3 + result1 + result2

    def __private_method(self):
        """Protected operation. CAN'T overriden."""
        this_method_name = sys._getframe().f_code.co_name
        return this_method_name

    def specific_processing_1(self):
        """You HAVE TO override this method in a subclass."""
        raise NotImplementedError

#    def specific_processing_2(self):

    def common_processings(self):
        """You CAN override this method. Here it ccntains common operations to perform in any case"""
        return "_TemplateMethod"


class Sibling1(Algorithm):
    def specific_processing_1(self):
        return "_SiblingClass1Method1"

    def specific_processing_2(self):
        return "_siblingClass1Method2"


class Sibling2(Algorithm):
    def specific_processing_1(self):
        return "_SiblingClass2Method1"

    def specific_processing_2(self):
        return "_siblingClass2Method2"

    def __private_method(self):
        return "FORBIDDEN"


class Test_Temp1lateMethodDesignPattern(unittest.TestCase):
    def test_shouldReturnSiblingClassResult_When_CallingTemplateMethodOnSiblingClass(self):
        sib1 = Sibling1()
        actual = sib1.template_method()

        self.assertEqual(actual, "...")

    def test_shouldReturnSiblingClassResult_When_CallingTemplateMethodOnSecondSiblingClass(self):
        sib1 = Sibling2()
        actual = sib1.template_method()

        self.assertEqual(actual, "...")

if __name__ == "__main__":
    unittest.main()