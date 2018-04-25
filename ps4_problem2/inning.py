from player import Player
from utility import Utility


class Inning:
    """
    Class to keep details of game like players, runs , wickets and so on
    """
    current_player = None
    other_player = None
    current_over = 0
    runs = 0
    current_ball_in_over = 0

    def __init__(self, total_overs, total_wickets, players_list, team_name, first_inning=False, target_runs=0):
        """
        initialize game with some initial data
        :param total_overs: total overs in the start
        :param total_wickets: total wickets in the game
        :param players_list: players in the team
        :param first_inning: tells the game, first inning or second inning
        :param target_runs: if this inning is second than we will give target runs to chase
        """
        self.players_list = players_list
        self.overs_left = total_overs
        self.wickets_left = total_wickets
        self.target_runs = target_runs
        self.out_batsman_list = []
        self.current_playing_batman_list = []
        self.team_name = team_name
        self.first_inning = first_inning
        self.second_inning = not first_inning
        self.set_first2_players()

    def set_first2_players(self):
        """
        gets opening pair of players from players list to play the match,
        the players will be instance of Player class
        """
        if self.current_player is None:
            self.current_player = Player(self.players_list.pop())
            self.current_player.set_probabilities_of_shot(Utility.assign_probability(self.current_player.prob_list))
            self.other_player = Player(self.players_list.pop())
            self.other_player.set_probabilities_of_shot(Utility.assign_probability(self.other_player.prob_list))
            # setting current players whom are on ground
            self.current_playing_batman_list = [self.current_player, self.other_player]

    def after_wicket_fall(self, out_batsman):
        """
        adds recent out batsman to out batsman list and counts down the wickets_left variable.
        gets new batsman from playerlist, unless player list is not empty
        :param out_batsman: the batsman who just got out
        :return True if new batsman added, false if there is no more player in list/ all out
        """
        self.wickets_left -= 1
        self.current_playing_batman_list.remove(out_batsman)
        self.out_batsman_list.append(out_batsman)
        if len(self.players_list) > 0:
            self.current_player = Player(self.players_list.pop())
            self.current_player.set_probabilities_of_shot(Utility.assign_probability(self.current_player.prob_list))
            self.current_playing_batman_list.append(self.current_player)
            return True
        return False

    def switch_batsmen_sides(self):
        """
        switches batsman sides
        """
        self.current_player, self.other_player = self.other_player, self.current_player

    def add_runs(self, runs):
        """
        In the case of first innings, we will add runs from required runs
        :param runs: runs scored by a batsman
        """
        self.runs += runs
        if self.second_inning:
            self.target_runs -= runs

    def change_over(self):
        """
        subtract over after each over, increases current over counter,
         changes strikes of players, and also prints summary of over and required runs.
        """
        self.overs_left -= 1
        self.current_over += 1
        self.current_ball_in_over = 0
        self.switch_batsmen_sides()
