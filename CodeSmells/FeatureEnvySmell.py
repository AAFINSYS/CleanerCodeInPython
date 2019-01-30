import unittest


class Phone(object):
    def __init__(self, country_prefix, number):
        self.country_prefix = country_prefix
        self.number = number


class Customer(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def getPhoneNumber(self):
        return self.phone.country_prefix + self.phone.number

    def __str__(self):
        return 'phone number for %s is %s' % (self.name, self.phone.country_prefix + self.phone.number)


class Test_FeatureEnvy(unittest.TestCase):
    def test_should_return_customer_phone_number_when_customer_is_asked_for_phone_number(self):
        phone = Phone(country_prefix="33", number=" 7 23 56 67 89")

        customer = Customer("John", phone)

        actual = customer.getPhoneNumber()

        self.assertEqual(actual, "33 7 23 56 67 89")
        self.assertEqual(str(customer), "phone number for John is 33 7 23 56 67 89")

if __name__ == "__main__":
    unittest.main()