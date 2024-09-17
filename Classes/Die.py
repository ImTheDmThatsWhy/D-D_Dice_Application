import random
#gives access to randint function to generate random numbers
class UserInput:
    def __init__(self, dice):
        self.dice = input("type in d2, d4, d6, d8, d10, d12, and d100")
        if dice == "d2":
            print(random.randint(1,2))
        elif dice == "d4":
            print(random.randint(1,4))
