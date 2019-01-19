from StrategyDesignPattern.ClassicStrategyDesignPattern import *

#>> > joe = Customer('John Doe', 0)  # <1>
#>> > ann = Customer('Ann Smith', 1100)
#>> > cart = [LineItem('banana', 4, .5),  # <2>
#             ...         LineItem('apple', 10, 1.5),
#             ...         LineItem('watermellon', 5, 5.0)]
#>> > Order(joe, cart, FidelityPromo())  # <3>
#< Order
#total: 42.00
#due: 42.00 >
#>> > Order(ann, cart, FidelityPromo())  # <4>
#< Order
#total: 42.00
#due: 39.90 >
#>> > banana_cart = [LineItem('banana', 30, .5),  # <5>
#                    ...                LineItem('apple', 10, 1.5)]
#>> > Order(joe, banana_cart, BulkItemPromo())  # <6>
#< Order
#total: 30.00
#due: 28.50 >
#>> > long_order = [LineItem(str(item_code), 1, 1.0)  # <7>
#                       ... for item_code in range(10)]
#>> > Order(joe, long_order, LargeOrderPromo())  # <8>
#< Order
#total: 10.00
#due: 9.30 >
#>> > Order(joe, cart, LargeOrderPromo())
#< Order
#total: 42.00
#due: 42.00 >

import unittest

class Test_ClassicStrategyDesignPattern(unittest.TestCase):
    def test_shouldReturnCorrectCartAmount_When_NoDiscountIsApplicable(self):
        cart = [LineItem('banana', 4, .5),
                LineItem('apple', 10, 1.5),
                LineItem('watermellon', 5, 5.0)]

        joe = Customer('John Doe', 0)

        order = Order(joe, cart, FidelityPromo())

        self.assertEqual(order.due(), 42)
        self.assertEqual(order.total(), 42)

if __name__ == "__main__":
    unittest.main()