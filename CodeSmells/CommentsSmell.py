import unittest

#The game consists of 10 frames.  In each frame the player has two opportunities to knock down 10 pins.
#The score for the frame is the total number of pins knocked down, plus bonuses for strikes and spares.

#A spare is when the player knocks down all 10 pins in two tries.  The bonus for that frame is the number
#of pins knocked down by the next roll.

#A strike is when the player knocks down all 10 pins on his first try.  The bonus for that frame is the
#value of the next two balls rolled.

#In the tenth frame a player who rolls a spare or strike is allowed to roll the extra balls to complete
#the frame. However no more than three balls can be rolled in tenth frame.


#Requirements:

#Write a class named “Game” that has two methods:
#    roll(pins) is called each time the player rolls a ball. The argument is the number of pins knocked down.
#    score() is called only at the very end of the game. It returns the total score for that game.


class Game(object):

    def __init__(self):
        # this array contains each roll score (the number of pins that are down after the ball has rolled)
        self.my_private_array = []

    def roll(self, pins):
        self.my_private_array.append(pins)

    def score(self):
        # score of the bowling game
        return_result = 0
        # index of the current frame
        current_index = 0

        # looping of all the 10 frames
        for current_iteration in range(10):
            # testing for a strike
            if self.my_private_array[current_index] == 10:
                return_result += 10 + self.my_private_array[current_index + 1] + self.my_private_array[current_index + 2]
                current_index += 1
            # testing for a spare
            elif self.my_private_array[current_index] + self.my_private_array[current_index+1] == 10:
                return_result += 10 + self.my_private_array[current_index + 2]
                current_index += 2
            # no strike, no spare (too bad for you)
            else:
                return_result += self.my_private_array[current_index] + self.my_private_array[current_index + 1]
                current_index += 2
        return return_result


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_gutter_game(self):
        self._roll_many(0, 20)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        self._roll_many(1, 20)
        self.assertEqual(20, self.game.score())

    def test_one_spare(self):
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(0, 17)
        self.assertEqual(16, self.game.score())

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(0, 16)
        self.assertEqual(24, self.game.score())

    def test_perfect_game(self):
        self._roll_many(10, 12)
        self.assertEqual(300, self.game.score())

    def test_simple_game(self):
        for pins in [1, 4, 4, 5, 6, 4, 5, 5,
                     10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]:
            self.game.roll(pins)
        self.assertEqual(133, self.game.score())

    def _roll_many(self, pins, num):
        for i in range(num):
            self.game.roll(pins)

    def _roll_spare(self):
        self.game.roll(8)
        self.game.roll(2)


if __name__ == "__main__":
    unittest.main()