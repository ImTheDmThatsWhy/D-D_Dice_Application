#first going to set up the welcome to app message and import color module which will make terminal easier to read.
from colored import Fore, Back, Style
# from requirements.txt import black 

print(f"{Fore.red}{Back.black}Welcome to the D&D Dice Application{Style.reset}\n")
#next step is to create a menu for the user to use.

def main_menu():
    print("Enter 1 to roll dice")
    print("Enter 2 to roll a d20 with advantage or disadvantage")
    print("Enter 3 to view saved combo's")
    print("Enter 4 to exit the app")
    choice = input("Enter your choice:")
    return choice

