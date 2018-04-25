import random

# let's define team choices for given circumstances
teams = [{"name": "Lengaburu", "Clear": "Bats", "Cloudy": "Bowls",
          "Day": "Bats", "Night": "Bowls"},
          {"name": "Enchai", "Clear": "Bowls", "Cloudy": "Bats",
           "Day": "Bowls", "Night": "Bats"}]

# let's take input from user
input_weather = input()
two_conditions = input_weather.split(" ")



def tossResult(conditions):
    """Takes conditons of the day and returns the result on the basis of toss and
    previous match history."""
    # We will select a random number between 0 to 99 and we will decide from
    # this that who will win the toss.
    toss_random_generation = random.randint(0, 100)
    winner = None
    if toss_random_generation > 49:
        winner = teams[0]
    else:
        winner = teams[1]
    result_based_on_weather = winner[conditions[0]]
    result_based_on_day_time = winner[conditions[1]]

    if result_based_on_day_time == result_based_on_weather:
        return_string = winner['name'] + " wins toss and " +\
                        result_based_on_weather.lower()
        return return_string
    else:
        return_string = winner['name'] + " wins toss and bats"
        return return_string


print(tossResult(two_conditions))
