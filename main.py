# first going to set up the welcome to app message and import color module which will make terminal easier to read.
from colored import Fore, Back, Style
from functions.roll_dice_functions import roll_dice
from functions.disadvantage_and_advantage_rolls import advantage_disadvantage_menu
from saved.saving import combo_and_save
from functions.print_cheat_sheet import print_sheet_delete

print(f"{Fore.red}{Back.black}Welcome to the D&D Dice Application{Style.reset}\n")


def main_menu():
    print("Enter 1 to roll dice")
    print("Enter 2 to roll d20 with advantage or disadvantage")
    print("Enter 3 to create a dice combination to save to create a cheatsheet")
    print("Enter 4 to view saved dice combinations and edit dice combinations")
    print("Enter 5 to exit")
    choice = input("Enter your choice:")
    return choice


choice = ""
while choice != "5":
    choice = main_menu()
    if choice == "1":
        print(
            f"{Fore.red}{Back.black}Choose your dice and the number of dice you wish to roll{Style.reset}\n"
        )
        roll_dice()
    elif choice == "2":
        print(
            f"{Fore.red}{Back.black}Roll with Advantage or Disadvantage{Style.reset}\n"
        )
        advantage_disadvantage_menu()
    elif choice == "3":
        combo_and_save()
        print("Create your dice combination")
    elif choice == "4":
        print(f"{Fore.red}{Back.black}Showing your saved combinations:{Style.reset}\n")
        print_sheet_delete()
    elif choice == "5":
        print(f"{Fore.red}{Back.black}Exiting{Style.reset}\n")
    else:
        print(f"{Fore.red}Invalid choice{Style.reset}\n")
print(f"{Fore.red}{Back.black}Thank you for using the D&D Dice App{Style.reset}\n")
