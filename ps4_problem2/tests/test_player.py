import sys
sys.path.insert(0, '../')
from player import Player
import unittest
from utility import Utility

class TestStringMethods(unittest.TestCase):

    def test_player_shot_on_ball(self):
        """
        checking player plays a shot from [0, 1, 2, 3, 4, 5, 6, 7]
        """
        player = Player({'name': "Vic", "prob_list": [10, 5, 5, 20, 7, 7, 30, 16]})
        player.set_probabilities_of_shot(Utility.assign_probability(player.prob_list))
        value = player.play_a_ball()
        value_truth = value in [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertTrue(value_truth, True)


if __name__ == "__main__":
    unittest.main()
