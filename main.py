# first going to set up the welcome to app message and import color module which will make terminal easier to read.
from colored import Fore, Back, Style
from Classes.Dice import roll_dice

# from requirements.txt import black

print(f"{Fore.red}{Back.black}Welcome to the D&D Dice Application{Style.reset}\n")
# next step is to create a menu for the user to use.


def main_menu():
    print("Enter 1 to roll dice")
    print("Enter 2 to roll a d20 with advantage or disadvantage")
    print("Enter 3 to create a dice combination to save")
    print("Enter 4 to view saved dice combinations")
    print("Enter 5 to exit the app")
    choice = input("Enter your choice:")
    return choice


choice = ""
while choice != "5":
    choice = main_menu()
    if choice == "1":
        roll_dice()
        print("Choose your dice and the number of dice you wish to roll")
    elif choice == "2":
        print("Roll with Advantage or Disadvantage")
    elif choice == "3":
        print("Create your dice combination")
    elif choice == "4":
        print("Showing your saved combinations:")
    else:
        print("Invalid choice")
print("Thank you for using the D&D Dice App")
