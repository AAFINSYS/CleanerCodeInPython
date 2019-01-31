import unittest


def get_roman_numeral(number):
    numeral = ''

    while number >= 1000:
        numeral += 'M'
        number -= 1000

    if number >= 900 and number < 1000:
        numeral += 'CM'
        number -= 900

    while number >= 500:
        numeral += 'D'
        number -= 500

    if number >= 400 and number < 500:
        numeral += 'CD'
        number -= 400

    while number >= 100:
        numeral += 'C'
        number -= 100

    if number >= 90 and number < 100:
        numeral += 'XC'
        number -= 90

    while number >= 50:
        numeral += 'L'
        number -= 50

    if number >= 40 and number < 50:
        numeral += 'XL'
        number -= 40

    while number >= 10:
        numeral += 'X'
        number -= 10

    if number == 9:
        numeral += 'IX'
        number -= 9

    if number >= 5:
        numeral += 'V'
        number -= 5

    if number == 4:
        numeral += 'IV'
        number -= 4

    while number >= 1:
        numeral += 'I'
        number -= 1

    return numeral


class TestRomanNumeralsConvertToRoman(unittest.TestCase):
    def test_one(self):
        result = get_roman_numeral(1)
        self.assertEqual('I', result)

    def test_ten(self):
        result = get_roman_numeral(10)
        self.assertEqual('X', result)

    def test_five(self):
        result = get_roman_numeral(5)
        self.assertEqual('V', result)

    def test_seven(self):
        result = get_roman_numeral(7)
        self.assertEqual('VII', result)

    def test_sixteen(self):
        result = get_roman_numeral(16)
        self.assertEqual('XVI', result)

    def test_twenty_eight(self):
        result = get_roman_numeral(28)
        self.assertEqual('XXVIII', result)

    def test_four(self):
        result = get_roman_numeral(4)
        self.assertEqual('IV', result)

    def test_four(self):
        result = get_roman_numeral(9)
        self.assertEqual('IX', result)

    def test_thirty_nine(self):
        result = get_roman_numeral(39)
        self.assertEqual('XXXIX', result)

    def test_thirty_four(self):
        result = get_roman_numeral(34)
        self.assertEqual('XXXIV', result)

    def test_fifty(self):
        result = get_roman_numeral(50)
        self.assertEqual('L', result)

    def test_fifty_nine(self):
        result = get_roman_numeral(59)
        self.assertEqual('LIX', result)

    def test_one_hundred(self):
        result = get_roman_numeral(100)
        self.assertEqual('C', result)

    def test_five_hundred(self):
        result = get_roman_numeral(500)
        self.assertEqual('D', result)

    def test_one_thousand(self):
        result = get_roman_numeral(1000)
        self.assertEqual('M', result)

    def test_eighty_eight(self):
        result = get_roman_numeral(88)
        self.assertEqual('LXXXVIII', result)

    def test_eighty_nine(self):
        result = get_roman_numeral(89)
        self.assertEqual('LXXXIX', result)

    def test_nineteen(self):
        result = get_roman_numeral(19)
        self.assertEqual('XIX', result)

    def test_ninety(self):
        result = get_roman_numeral(90)
        self.assertEqual('XC', result)

    def test_fourty(self):
        result = get_roman_numeral(40)
        self.assertEqual('XL', result)

    def test_four_hundred_and_fourty_eight(self):
        result = get_roman_numeral(448)
        self.assertEqual('CDXLVIII', result)

    def test_nineteen_eighty_nine(self):
        result = get_roman_numeral(1989)
        self.assertEqual('MCMLXXXIX', result)

    def test_nine_hundred_and_ninety(self):
        result = get_roman_numeral(990)
        self.assertEqual('CMXC', result)

    def test_nineteen_ninety(self):
        result = get_roman_numeral(1990)
        self.assertEqual('MCMXC', result)

    def test_nineteen_ninety_nine(self):
        result = get_roman_numeral(1999)
        self.assertEqual('MCMXCIX', result)

    def test_two_thousand_and_eight(self):
        result = get_roman_numeral(2008)
        self.assertEqual('MMVIII', result)

    def test_two_thousand_nine_hundred_and_ninety(self):
        result = get_roman_numeral(2990)
        self.assertEqual('MMCMXC', result)

    def test_two_thousand_nine_hundred_and_ninety_nine(self):
        result = get_roman_numeral(2999)
        self.assertEqual('MMCMXCIX', result)

    def test_two_thousand_four_hundred_and_fourty_four(self):
        result = get_roman_numeral(2444)
        self.assertEqual('MMCDXLIV', result)

    def test_three_thousand(self):
        result = get_roman_numeral(3000)
        self.assertEqual('MMM', result)

    def test_five_thousand_four_hundred_and_ninety_four(self):
        result = get_roman_numeral(5494)
        self.assertEqual('MMMMMCDXCIV', result)


if __name__ == "__main__":
    unittest.main()