import unittest
import datetime

def call_my_complicated_boolean_expresion_example_function(processing, pricingAsOfDate, periodFixingDate, applyFixing, fixingAvailable):
    if (processing == "Valuation" and pricingAsOfDate > periodFixingDate and fixingAvailable) or \
        (processing == "RiskAnalysis" and pricingAsOfDate > periodFixingDate and fixingAvailable and applyFixing) or \
        not(processing != "Valuation" or not fixingAvailable):
        return "correct answer"

    return "incorrect answer"

class TestComplicatedBooleanSmell(unittest.TestCase):
    def test_should_trigger_correct_response_when_complicated_boolean_expression_is_processed(self):
        actual = call_my_complicated_boolean_expresion_example_function("Valuation", datetime.date(2019, 1, 12), datetime.date(2019, 1, 11), True, True)

        self.assertEqual(actual, "correct answer")

if __name__ == "__main__":
    unittest.main()