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
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def total_score(self):
        score = 0
        roll_index = 0
        for frame in range(10):
            if self.rolls[roll_index] == 10:
                score += 10 + self.rolls[roll_index+1] + self.rolls[roll_index+2]
                roll_index += 1
            elif self.rolls[roll_index] + self.rolls[roll_index+1] == 10:
                score += 10 + self.rolls[roll_index+2]
                roll_index += 2
            else:
                score += self.rolls[roll_index] + self.rolls[roll_index+1]
                roll_index += 2
        return score


class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_gutter_game(self):
        self._roll_many(0, 20)
        self.assertEqual(0, self.game.total_score())

    def test_all_ones(self):
        self._roll_many(1, 20)
        self.assertEqual(20, self.game.total_score())

    def test_one_spare(self):
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(0, 17)
        self.assertEqual(16, self.game.total_score())

    def test_one_strike(self):
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(0, 16)
        self.assertEqual(24, self.game.total_score())

    def test_perfect_game(self):
        self._roll_many(10, 12)
        self.assertEqual(300, self.game.total_score())

    def test_simple_game(self):
        for pins in [1, 4, 4, 5, 6, 4, 5, 5,
                     10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]:
            self.game.roll(pins)
        self.assertEqual(133, self.game.total_score())

    def _roll_many(self, pins, num):
        for i in range(num):
            self.game.roll(pins)

    def _roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)


if __name__ == "__main__":
    unittest.main()