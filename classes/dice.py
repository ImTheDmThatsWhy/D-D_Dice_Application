import random


# This class refers to the number of faces a dice has based on a given input, and will return a random interger based on the given in input
class Dice:
    def __init__(self, value):
        self.value = value

    def roll(self):
        return random.randint(1, self.value)
