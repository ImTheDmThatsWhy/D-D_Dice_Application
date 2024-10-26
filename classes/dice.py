import random


class Dice:
    def __init__(self, value):
        self.value = value

    def roll(self):
        return random.randint(1, self.value)
