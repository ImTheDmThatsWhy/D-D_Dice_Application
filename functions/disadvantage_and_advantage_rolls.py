from functions.roll_dice_functions import advantage, disadvantage
from colored import Fore, Style

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
