# The random module has been imported so that a random number be returned in the dice class from the range of the given input for example if the input is 6, then the random.randomint will return a random interger between 1-6.
import random


# This class refers to the number of faces a dice has based on a given input, and will return a random interger based on the given in input
class Dice:
    def __init__(self, value):
        self.value = value

    def roll(self):
        return random.randint(1, self.value)
