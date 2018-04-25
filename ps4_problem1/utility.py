

class Utility:
    """
    some utility functions that can be used while playing inning in a cricket
    """
    @staticmethod
    def assign_probability(prob_list):
        """takes a probability list of a player and
        makes a distribution of probability in a new list from 0 to 99
        input: a list of probabilities
        return: a list of probabilities distributed from 0 to 99"""
        count_prob = 0
        prob_list_of_shots = []
        for ball in prob_list:
            range_tuple=(count_prob, count_prob+ball-1)
            count_prob += ball
            prob_list_of_shots.append(range_tuple)
        return prob_list_of_shots

    @staticmethod
    def score_run(inning, batsman_action):
        """
        procedure when batsman scores any run from [0,1,2,3,4,5,6]
        :param inning: set up of a inning(wickets, overs, players etc information)
        :param batsman_action: what did batsman did on last ball
        :return: 1 if team has won the match otherwise 0
        """
        print(str(inning.current_over) + "." + str(inning.current_ball_in_over) + " " +
              inning.current_player.name + " scores " + str(batsman_action) + " runs.")
        inning.add_runs(batsman_action)
        if batsman_action % 2 != 0:
            # if numbers scored by player is odd, then it's time to change strike.
            inning.switch_batsmen_sides()

    @staticmethod
    def batsman_out(inning):
        """
        procedure when batsman gets out.
        :param inning: set up of a inning(wickets, overs, players etc information)
        :return: return 0 if team haven't lost all the wickets, 1 if team has lost all the wicket
        """
        print(str(inning.current_over) + "." + str(inning.current_ball_in_over) +
              " " + inning.current_player.name + " gets Out.")
        # adds out batsman to out batsman list and let's see there is another wicket left or not
        wickets_left = inning.after_wicket_fall(inning.current_player)
        if wickets_left:
            return 0
        else:
            return 1

    @staticmethod
    def after_over(inning):
        inning.change_over()
        if inning.first_inning:
            print()
            print(str(inning.overs_left) + " Overs are remaining and score is  " +
                  str(inning.runs) + " runs\n")
        else:
            print()
            print(str(inning.overs_left) + " Overs are remaining and needed " +
                  str(inning.target_runs) + " runs to win.\n")

    @staticmethod
    def after_inning(inning):
        """
        result after completing an inning
        :param inning: set up of a inning(wickets, overs, players etc information)
        :return: inning object for both innings for second inning boolean value for win or lost, and one another
        boolean value for tie example: return inning, True, False // first boolean is for win, and second is for tie.
        """
        # after player all overs
        if inning.first_inning:
            return inning
        else:
            if inning.target_runs == 1:
                # if runs needed to win is 1. That's mean match's result is a tie.
                return inning, False, True
            else:
                # overs are completed. But required runs are not made by the team. So team has lost the match
                return inning, False, False

    @staticmethod
    def print_player_record(inning):
        """
        prints the records of players
        :param inning: inning information at current time
        """
        print("-----Score-card-----")
        print("Team Name : " + inning.team_name + " || Total-score:" + str(inning.runs))
        for player in inning.out_batsman_list:
            # prints out player score card of players for out batsmen
            print(player.name + " - " + str(player.run_scored) +
                  " (" + str(player.ball_played) + " balls)")
        for player in inning.current_playing_batman_list:
            # prints current player score card of players for not out batsmen
            print(player.name + " - " + str(player.run_scored) +
                  "* (" + str(player.ball_played) + " balls)")

    @staticmethod
    def result(won, inning, tie=None):
        """
        prints summary of match after winning and losing
        :param won: won or loss boolean value
        :param inning: inning object, details about inning
        :param tie: if match got tie, this will be true
        """
        Utility.print_player_record(inning)
        print("\nRESULT:")
        if won:
            # The team won the match, let's arrange the result string.
            balls_remaining = (inning.overs_left + inning.current_over) * 6 - (inning.current_over * 6 + inning.current_ball_in_over)
            print(inning.team_name + " won by " + str(inning.wickets_left) + " wickets and with " +
                  str(int(balls_remaining / 6)) + "." + str((balls_remaining % 6)) + " overs remaining.")
        elif tie:
            print("Match got Tie")
        else:
            # The team lost the match,let's arrange the result string.
            print(inning.team_name + " lost by " + str(inning.target_runs) + " runs.")
        print()