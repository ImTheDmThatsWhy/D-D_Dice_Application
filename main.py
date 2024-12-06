# The colored module has been imported so that the error message can be colored red
# as demonstrated in the following code: print(f"{Fore.red}Invalid choice{Style.reset}\n")
# The colored module has also been used to color other messages as shown in the code below from print sheet delete:
#   print(
#         f"{Fore.red}{Back.black}Choose your dice and the number of dice you wish to roll{Style.reset}\n"
# The fore import stylizes the text while style.reset normalizes the text, and the back import colours the background.
# The colored module has been used in all functions
# listed below in the same manner as the code example above for error messages and print messages.
from colored import Fore, Back, Style
from functions.roll_dice_functions import roll_dice

# the advantage_disadvantage_menu has been imported so that when a user inputs option 2 the menu function activates.
from functions.disadvantage_and_advantage_rolls import advantage_disadvantage_menu
from saved.saving import combo_and_save
from functions.print_cheat_sheet import print_sheet_delete

print(
    f"{Fore.red}{Back.black}Welcome to the TableTop RPG Dice Roller Application{Style.reset}\n"
)


# function creates main menu interface that prints the options listed below, then prompts the user to input
# their preferred options and returns the inputted choice.

# Imports and modules:
# roll_dice(): imported from functions.roll_dice_functions and executes
#   a function that allow players to roll dice when option 1 is inputted.

# advantage_disadvantage_menu(): imported from functions.disadvantage_and_advantage_rolls
#   that executes a function that allows users to choose from a second menu to roll
#   with advantage or disadvantage.

# combo_and_save():imported from saved.saving the combo_and_save function has been imported
# so that when a person selects option 3 the function executes and they can create a new combo to save to the cheatsheet.

# print_sheet_delete(): imported from functions.print_cheat_delete,
# the print_sheet_delete function has been imported so that when a person
# selects option 4 the print_sheet_delete function executes and they can view the
# cheat sheet then decide it they want to delete a saved entry.

# Colored: The imported colored functions Fore, back, and style are used as described above the import from colored code
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
print(
    f"{Fore.red}{Back.black}Thank you for using the TableTop RPG Dice Roller App{Style.reset}\n"
)


