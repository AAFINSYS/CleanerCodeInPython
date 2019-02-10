import unittest

from RefactoringKata.GildedRose.GildedRose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):
    def test_should_decrease_the_quality_of_an_apple_by_one_when_a_day_goes_by(self):
        items = [Item("apple", sell_in=5, quality=10)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 9)

    def test_should_decrease_the_sellIn_of_an_apple_by_one_when_a_day_goes_by(self):
        items = [Item("apple", sell_in=5, quality=10)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].sell_in, 4)

    def test_should_decrease_the_quality_of_an_apple_by_two_when_a_day_goes_by_and_sellIn_has_passed(self):
        items = [Item("apple", sell_in=-2, quality=10)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 8)

    def test_should_never_have_a_negative_quality_for_an_apple_when_a_day_goes_by(self):
        items = [Item("apple", sell_in=5, quality=0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 0)

    def test_should_increase_the_quality_of_an_aged_brie_by_one_when_a_day_goes_by(self):
        items = [Item("Aged Brie", sell_in=5, quality=15)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 16)

    def test_should_increase_the_quality_of_an_aged_brie_by_four_when_a_day_goes_by_and_the_sellin_has_passed(self):
        items = [Item("Aged Brie", sell_in=-2, quality=15)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 17)

    def test_should_never_have_the_quality_of_an_aged_brie_be_more_than_fifty_when_a_day_goes_by_and_sellin_is_positive(self):
        items = [Item("Aged Brie", sell_in=5, quality=50)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 50)

    def test_should_never_have_the_quality_of_an_aged_brie_be_more_than_fifty_when_a_day_goes_by_and_sellin_has_passed(self):
        items = [Item("Aged Brie", sell_in=-3, quality=50)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 50)

    def test_should_never_alter_the_quality_of_a_sulfuras_when_a_day_goes_by_and_the_sellin_is_positive(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=5, quality=80)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 80)

    def test_should_never_alter_the_quality_of_a_sulfuras_when_a_day_goes_by_and_the_sellin_has_passed(self):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in=-5, quality=80)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 80)

    def test_should_increase_the_quality_of_a_backstage_by_one_when_a_day_goes_by_and_the_sellin_is_more_than_ten(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=12, quality=22)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 23)

    def test_should_increase_the_quality_of_a_backstage_by_two_when_a_day_goes_by_and_the_sellin_is_between_six_and_ten(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=22)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 24)

    def test_should_increase_the_quality_of_a_backstage_by_two_within_thefifty_limit_when_a_day_goes_by_and_the_sellin_is_between_six_and_ten(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=49)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 50)

    def test_should_increase_the_quality_of_a_backstage_by_three_when_a_day_goes_by_and_the_sellin_is_between_one_and_five(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=22)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 25)

    def test_should_increase_the_quality_of_a_backstage_by_three_within_the_fifty_limit_when_a_day_goes_by_and_the_sellin_is_between_one_and_five(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=49)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 50)

    def test_should_drop_the_quality_of_a_backstage_to_zero_when_a_day_goes_by_and_the_sellin_has_passed(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=-4, quality=22)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 0)

    def test_should_return_representation_string_when_asked(self):
        actual = str(Item("apple", sell_in=5, quality=10))

        self.assertEqual(actual, "apple, 5, 10")


if __name__ == '__main__':
    unittest.main()
