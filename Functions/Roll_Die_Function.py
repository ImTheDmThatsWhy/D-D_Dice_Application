import random
from colored import Fore, Style
def __init__(self, value):
       self.value=value
def roll(self):
       return random.randint(1,self.value)
def roll_two_dice():
    firstd20=random.randint(1, 20)
    secondd20=random.randint(1, 20)
    dice_list=[firstd20, secondd20]
    dice_list.sort()
    print(dice_list)
    return dice_list
def advantage():
    dice_list=roll_two_dice()
    print("Highest D20 roll is:",f"{Fore.blue}{dice_list[1]}{Style.reset}\n")

def disadvantage():
    dice_list=roll_two_dice()
    print("Lowest D20 roll is:",f"{Fore.red}{dice_list[0]}{Style.reset}\n")
