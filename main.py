# first going to set up the welcome to app message and import color module which will make terminal easier to read.
from colored import Fore, Back, Style
from Functions.Roll_Die_Function import roll_dice
from Classes.AdvantageDisadvantage import advantage_disadvantage_menu
from SavedDiceCombos.saving import combo_and_save

# from requirements.txt import black

print(f"{Fore.red}{Back.black}Welcome to the D&D Dice Application{Style.reset}\n")
# next step is to create a menu for the user to use.


def main_menu():
    print("Enter 1 to roll dice")
    print("Enter 2 to roll d20 with advantage or disadvantage")
    print("Enter 3 to create a dice combination to save")
    print("Enter 4 to view saved dice combinations")
    print("Enter 5 to exit the app")
    choice = input("Enter your choice:")
    return choice


choice = ""
while choice != "5":
    choice = main_menu()
    if choice == "1":
        print(f"{Fore.red}{Back.black}Choose your dice and the number of dice you wish to roll{Style.reset}\n")
        roll_dice()
    elif choice == "2":
        print(f"{Fore.red}{Back.black}Roll with Advantage or Disadvantage{Style.reset}\n")
        advantage_disadvantage_menu()
    elif choice == "3":
        combo_and_save()
        print("Create your dice combination")
    elif choice == "4":
        print(f"{Fore.red}{Back.black}Showing your saved combinations:{Style.reset}\n")
    elif choice == "5":
        print(f"{Fore.red}{Back.black}Exiting{Style.reset}\n")
    else:
        print("Invalid choice")
print(f"{Fore.red}{Back.black}Thank you for using the D&D Dice App{Style.reset}\n")
