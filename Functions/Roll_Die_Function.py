import random
from colored import Fore, Style
def __init__(self, value):
       self.value=value
def roll(self):
        return random.randint(1,self.value)
def advantage():
    firstd20=random.randint(1, 20)
    secondd20=random.randint(1, 20)
    dice_list=[firstd20, secondd20]
    print(dice_list)
    dice_list.sort()
    print("Highest D20 roll is:",f"{Fore.blue}{dice_list[1]}{Style.reset}\n")

def disadvantage():
    firstd20=random.randint(1, 20)
    secondd20=random.randint(1, 20)
    dice_list=[firstd20, secondd20]
    print(dice_list)
    dice_list.sort()
    print("Lowest D20 roll is:",f"{Fore.red}{dice_list[0]}{Style.reset}\n")
