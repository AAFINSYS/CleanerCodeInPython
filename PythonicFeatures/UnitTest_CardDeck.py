import unittest
from PythonicFeatures.CardDeck import FrenchDeck, Card

class Test_CardDeck(unittest.TestCase):
    def test_should_return_number_of_cards_when_the_deck_is_asked_for_it(self):
        deck = FrenchDeck()

        actual = 0

        self.assertEqual(actual, 52)

    def test_should_return_when_last_card_of_the_deck_is_looked_at(self):
        deck = FrenchDeck()

        actual = "..."

        self.assertEqual(actual.rank, 'A')
        self.assertEqual(actual.suit, 'hearts')


if __name__ == "__main__":
    unittest.main()