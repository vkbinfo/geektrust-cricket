import sys
sys.path.insert(0, '../')
from unittest import TestCase, main
from inning import Inning
from utility import Utility


class TestUtility(TestCase):
    def setUp(self):
        # some information to play cricket
        overs_in_match = 4
        wickets_remaining = 3
        runs_required_to_win = 40
        all_players = [
            {"name": "Kirat Boli", "prob_list": [5, 30, 25, 10, 15, 1, 9, 5]},
            {"name": "N.S Nodhi", "prob_list": [10, 40, 20, 5, 10, 1, 4, 10]},
            {"name": "R Rumrah", "prob_list": [20, 30, 15, 5, 5, 1, 4, 20]},
            {"name": "Shashi Henra", "prob_list": [30, 25, 5, 0, 5, 1, 4, 30]}
        ]
        all_players.reverse()
        self.inning = Inning(overs_in_match, wickets_remaining, all_players, "Lengaburu", target_runs=runs_required_to_win)
        self.utility = Utility

    def test_assign_probability(self):
        """
        checking about that function is distributing probability in
        rightful manner from 0 to 99
        """
        self.assertEqual(self.utility.assign_probability([10, 5, 5, 20, 7, 7, 30, 16]),
                        [(0, 9), (10, 14), (15, 19), (20, 39), (40, 46),
                         (47, 53), (54, 83), (84, 99)])

    def test_score_run(self):
        """
        checks that it subtracts the run or not
        """
        self.inning.add_runs(5)
        self.assertEqual(self.inning.runs, 5,
                         "after subtracting amount from inning.runs_to_win,"
                         " it is not same  as subtracting from real required run")

    def test_batsman_out(self):
        """checks the current batsman goes into out batsman list after getting out"""
        going_to_out_player = self.inning.current_player
        Utility.batsman_out(self.inning)
        self.assertEqual(self.inning.out_batsman_list[-1], going_to_out_player)

    def test_after_over(self):
        """changes overs and switches player sides"""
        current_over = self.inning.current_over
        old_current = self.inning.current_player
        old_other = self.inning.other_player
        self.inning.change_over()
        self.assertEqual(current_over + 1, self.inning.current_over,
                         "Current over not increased by 1 run")
        self.assertEqual(old_current, self.inning.other_player,
                         "old current/striker player and new other are not same.")
        self.assertEqual(old_other, self.inning.current_player,
                         "old other player and new current/striker are not same.")

    def test_after_inning(self):
        """Checking if match gets tie than it works ok"""
        self.inning.target_runs = 1
        _, _, tie = Utility.after_inning(self.inning)
        self.assertEqual(tie, True)

if __name__ == "__main__":
    main(buffer=True)

