# Random is a built in python class that has been imported so that a random
# number can be returned in the dice class from the range of the given input, so
# for example if the input is 6 then random.randomint will return an integer
# between 1-6.
import random


# This class refers to the number of faces on a die based on input,
# and will return a random integer based on input.
# Attributes:
#     value(int): the number of faces on the die
class Dice:
    # This function creates a dice where the
    #     value inputed is equal to the number
    #     of faces on the die.

    # Parametres:
    #     value (int): Refers to the value of
    #         the die
    def __init__(self, value):
        self.value = value

    # This function returns a random integer
    # (return random.randint) between 1 and the
    # value of the die (self.value).

    # Returns:
    #     Returns a random integer by using the built-in
    #     python random class with the command randint
    #     meaning a random integer between the values
    #     of 1 and the value of the die as shown below:
    #     return random.randint(1, self.value)
    def roll(self):
        return random.randint(1, self.value)
