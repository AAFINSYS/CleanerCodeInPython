from StrategyDesignPattern.ClassicStrategyDesignPattern import *
import unittest


class Test_ClassicStrategyDesignPattern(unittest.TestCase):
    def test_shouldReturnCorrectCartAmount_When_NoDiscountIsApplicable(self):
        cart = [LineItem('banana', 4, .5),
                LineItem('apple', 10, 1.5),
                LineItem('watermelon', 5, 5.0)]

        joe = Customer('John Doe', 0)

        order = Order(joe, cart, FidelityPromo())

        self.assertEqual(order.due(), 42)
        self.assertEqual(order.total(), 42)

if __name__ == "__main__":
    unittest.main()