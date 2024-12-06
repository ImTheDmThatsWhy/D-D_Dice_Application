# advantage, and disadvantage functions have been imported so that when users choose to roll with
# advantage or disadvantage the relevant function will execute as shown in the following code:
# if choice == "1":
#   print("Rolling with advantage")
#   advantage()

from functions.roll_dice_functions import advantage, disadvantage

# The colored module has been imported so that the error message in the advantage and disadvantage menu
# can be color coded red as shown in the following code:
# print(f"{Fore.red}invalid choice{Style.reset}\n").
# The fore import stylizes the text while style.reset normalizes the text
from colored import Fore, Style


# This function is a menu that gives users the choice to roll with advantage,
# disadvantage or exit by prompting users to input a choice using
# choice = "" and offers different choices in the form of elif conditons like the example below:
# if choice == "1":
#             print("Rolling with advantage")
#             advantage()
# elif choice == "2":
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
