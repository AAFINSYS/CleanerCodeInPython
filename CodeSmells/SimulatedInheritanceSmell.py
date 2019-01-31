import unittest


class Dog(object):
    pass


class Lion(object):
    pass


class Antelope(object):
    pass


class Badger(object):
    pass


def makeNoiseWithMouth(animal):
    if isinstance(animal, Dog):
        return "Barking!!!!"

    if isinstance(animal, Lion):
        return "Roaring!!!!"

    if isinstance(animal, Antelope):
        return "Snorting!!!!"

    if isinstance(animal, Badger):
        return "Growling!!!!"


class TestAnimalNoises(unittest.TestCase):
    def test_should_bark_when_a_dog_is_asked_to(self):
        dog = Dog()
        actual = makeNoiseWithMouth(dog)

        self.assertEqual(actual, "Barking!!!!")

    def test_should_roar_when_a_lion_is_asked_to(self):
        lion = Lion()
        actual = makeNoiseWithMouth(lion)

        self.assertEqual(actual, "Roaring!!!!")

    def test_should_snort_when_an_antelope_is_asked_to(self):
        antelope = Antelope()
        actual = makeNoiseWithMouth(antelope)

        self.assertEqual(actual, "Snorting!!!!")

    def test_should_growl_when_a_badger_is_asked_to(self):
        badger = Badger()
        actual = makeNoiseWithMouth(badger)

        self.assertEqual(actual, "Growling!!!!")

if __name__ == "__main__":
    unittest.main()