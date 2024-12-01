from functions.roll_dice_functions import advantage, disadvantage
from colored import Fore, Style


# This function is a menu option that is a main menu in the app that gives the user the choice to roll with advantage, disadvantage or exit. If a user selects advantage or disadvantage, then the respective functions are called.
def advantage_disadvantage_menu():
    choice = ""
    while choice != "3":
        print("Enter 1 roll with advantage")
        print("Enter 2 to roll with disadvantage")
        print("Enter 3 to exit\n")
        choice = input("Enter your choice:\n")
        if choice == "1":
            print("Rolling with advantage")
            advantage()
        elif choice == "2":
            print("Rolling with disadvantage")
            disadvantage()
        elif choice == "3":
            print("exit")
        else:
            print(f"{Fore.red}invalid choice{Style.reset}\n")
