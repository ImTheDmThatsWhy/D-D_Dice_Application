import random
#gives access to randint function to generate random numbers
class UserInput:
    def __init__(self, dice):
        self.dice = input("type in d2, d4, d6, d8, d10, d12, d20, and d100")
        if dice == "d2":
            print(random.randint(1,2))
        elif dice == "d4":
            print(random.randint(1,4))
        elif dice == "d6":
            print(random.randint(1,6))
        elif dice == "d8":
            print(random.randint(1,8))
        elif dice == "d10":
            print(random.randint(1,10))
        elif dice == "d12":
            print(random.randint(1,12))
        elif dice == "d20":
            print(random.randint(1,20))
        elif dice == "d100":
            print(random.randint(1,100))
        else:
            print("Please make a valid selection")

