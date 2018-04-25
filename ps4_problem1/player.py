import random


class Player:
    """Information about player and methods for playing a ball """
    run_scored = 0
    ball_played = 0
    prob_list_of_shots = []

    def __init__(self, info_dict):
        """
        initializing player with its name and it's probability list
        :param info_dict:
        """
        self.name = info_dict['name']
        self.prob_list = info_dict["prob_list"]

    def set_probabilities_of_shot(self, prob_list_shots):
        """
        stores information about the player, the probability from 0 to 99 for each shot and out
        :param prob_list_shots: probability distribution of the player from 0 to 99
        """
        self.prob_list_of_shots = prob_list_shots

    def play_a_ball(self):
        """
        current players plays on ball, and on the value of random value and probability of the player
        We will get what player is going to play.
        :return: returns from [0,1,2,3,4,5,6,7] , 0 means no run and 7 means out
        """
        random_value = random.randint(0,99)
        for x in range(len(self.prob_list_of_shots)):
            range_tuple = self.prob_list_of_shots[x]
            if range_tuple[0] <= random_value <= range_tuple[1]:
                if x != 7:
                    self.run_scored = self.run_scored + x
                self.ball_played = self.ball_played + 1
                return x

