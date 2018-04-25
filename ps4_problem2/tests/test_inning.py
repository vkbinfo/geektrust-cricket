import sys
sys.path.append('../')
from unittest import TestCase, main
from inning import Inning


class Testinning(TestCase):
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

    def test_set_current_players(self):
        """
         verify that there are two batsman currently
        playing on the crease, kirat Boli and N.S Nodhi
        """
        self.assertEqual(self.inning.current_player.name, "Kirat Boli",
                         " The Initalization of first batsman is wrong")
        self.assertEqual(self.inning.other_player.name, "N.S Nodhi",
                         " The Initalization of second other batsman is wrong")

    def test_batsman_out_function(self):
        """
        checks if out function works or not.
        """
        self.inning.after_wicket_fall(self.inning.current_player)
        self.assertEqual(self.inning.out_batsman_list[0].name, "Kirat Boli",
                         "Kirat Boli must be in out_batsman_list at index 0, but it is not")

    def test_switch_batsmen_sides(self):
        """
         Switches current and other batsman
        """
        old_current = self.inning.current_player
        old_other = self.inning.other_player
        self.inning.switch_batsmen_sides()
        self.assertEqual(old_current, self.inning.other_player,
                         "old current/striker player and new other are not same.")
        self.assertEqual(old_other, self.inning.current_player,
                         "old other player and new current/striker are not same.")

    def test_add_runs(self):
        """
        checks that it subtracts the run or not
        """
        self.inning.add_runs(5)
        self.assertEqual(self.inning.runs, 5,
                         "after subtracting amount from inning.runs_to_win,"
                         " it is not same  as subtracting from real required run")

    def test_change_over(self):
        """changes overs and switches player sides"""
        current_over = self.inning.current_over
        old_current = self.inning.current_player
        old_other = self.inning.other_player
        self.inning.change_over()
        self.assertEqual(current_over+1, self.inning.current_over,
                         "Current over not increased by 1 run")
        self.assertEqual(old_current, self.inning.other_player,
                         "old current/striker player and new other are not same.")
        self.assertEqual(old_other, self.inning.current_player,
                         "old other player and new current/striker are not same.")


if __name__ == "__main__":
    main()
