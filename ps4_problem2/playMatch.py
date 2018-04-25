from inning import Inning
from utility import Utility

# information about teams to play cricket match
overs_in_match = 1
wickets = 1
team1_players = [{"name": "Kirat Boli", "prob_list": [5, 10, 25, 10, 25, 1, 14, 10]},
                 {"name": "N.S Nodhi", "prob_list": [5, 15, 15, 10, 20, 1, 19, 15]}
                 ]
team2_players = [{"name": "DB Vellyers", "prob_list": [5, 10, 25, 10, 25, 1, 14, 10]},
                 {"name": "H Mamla", "prob_list": [10, 15, 15, 10, 20, 1, 19, 10]}
                 ]
team1_players.reverse()
team2_players.reverse()


class Match:
    """
    Class to play Cricket Match.
    """
    OUT_NUMBER = 7

    def first_inning(self, inning):
        """
        plays first inning of a Match
        :param inning: First inning setting object containing all the information about players, wicket and other info
        :return: inning object after completing first inning that contains total score made by first inning team
        """
        return self.play_inning(inning)

    def second_inning(self, inning):
        """
        plays second inning of a Match
        :param inning: second inning setting object containing all the information about players, wicket and other info"""
        inning, won, tie = self.play_inning(inning)
        Utility.result(won, inning, tie=tie)

    def play_inning(self, inning):
        """
        playes a inning for given set of players and overs in inning object
        :param inning: set up of a inning(wickets, overs, players etc information)
        :return: inning object for both innings for second inning boolean value for win or lost, and one another boolean value
        for tie example: return inning, True, False // first boolean is for win, and second is for tie.
        """
        while inning.overs_left:
            # let's bowl an over
            for ball in range(1, 7):
                inning.current_ball_in_over = ball
                batsman_action = inning.current_player.play_a_ball()
                if batsman_action != self.OUT_NUMBER:
                    Utility.score_run(inning, batsman_action)
                    if inning.second_inning and inning.target_runs <= 0:
                        # Second team won
                        return inning, True, False
                if batsman_action == self.OUT_NUMBER:
                    all_out = Utility.batsman_out(inning)
                    if all_out:
                        return Utility.after_inning(inning)
            Utility.after_over(inning)
        return Utility.after_inning(inning)


if __name__ == "__main__":
    match = Match()
    first_inning_info = Inning(overs_in_match, wickets, team1_players,"Lengaburu",first_inning=True)
    # play first inning with the first inning_info object
    inning_result = match.first_inning(first_inning_info)
    # first inning info(overs, wicket, players etc.. we will store in a Inning object and
    # we will pass this info into match.second_inning
    inning2 = Inning(overs_in_match, wickets, team2_players, "Enchai", target_runs=inning_result.runs)
    match.second_inning(inning2)
