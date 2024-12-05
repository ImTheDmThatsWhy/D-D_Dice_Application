# saved_combo, and save_and_exit have been imported from saved.saving to be used in the relevant functions explained below.
from saved.saving import saved_combo, save_and_exit

# The colored module has been imported so that the error message can be colored red
# as demonstrated in the following code:
# print (f"{Fore.red}Dictionary is empty please got to main menu option 3 to create input{Style.reset}\n"
# The colored module has also been used to color other messages as shown in the code below from print sheet delete:
# print(f"{Fore.green}{saved_combinations}{Style.reset}\n").
# The fore import stylizes the text while style.reset normalizes the text. The colored module has been used in all functions
# listed below in the same manner as the code example above for error messages and print messages.
from colored import Fore, Style
from classes.exceptions import InappropriateInput


# This function is designed to delete items in the dictionary, saved_combinations refers to the json dictionary that contains the items, and saved_combo(saved_combinations) calls the saved dictionary. If the dictionary is empty (if saved_combinations =={}:) then an error message prints, else if the items in the dictionary exist then the delete items function (delete_items()) will be called.
# Modules and Imports:

# colored: The imported colored functions Fore, and style are used as described above the import from colored code


def print_sheet_delete():
    saved_combinations = {}
    saved_combo(saved_combinations)
    if saved_combinations == {}:
        print(
            f"{Fore.red}Dictionary is empty please got to main menu option 3 to create input{Style.reset}\n"
        )
    else:
        print(f"{Fore.green}{saved_combinations}{Style.reset}\n")
        delete_items()


# This function behaves in the same way as the function above however, on the else statement it prints the dictionary.
# Modules and Imports:


# colored: The imported colored functions Fore, and style are used as described above the import from colored code
def print_sheet():
    saved_combinations = {}
    saved_combo(saved_combinations)
    if saved_combinations == {}:
        print(
            f"{Fore.red}Dictionary is empty please got to main menu option 3 to create input{Style.reset}\n"
        )
    else:
        print(f"{Fore.green}{saved_combinations}{Style.reset}\n")


# This function deletes items from the existing dictionary, the user is offered the option to delete items.
# For options, a while loop is used as delete is equal to input. If Y is selected then the items are deleted
# by first loading the dictionary using saved_combo(imported from saved.saving) then the user is prompted to
# input a combo for deletion using combo = input ("enter name of combo you with to delete: "), the saved combo
# is then deleted using saced_combinations.pop(combo), where pop is a command that deletes an item in a dictionary.
# The new dictionary is then saved using save_and_exit(saved_combinations) (save_and_exit is imported from
# saved.saving) which saves the appended dictionary to the saved_combinations JSON file.
# Imports and Modules:
#
# Colored: The imported colored functions Fore, and style are used as described above the import from colored code
#
# Exceptions:
# InnapropriateInput
# The code is wrapped in a try block and the code
# raise InappropriateInput(
# f"{Fore.red}Please enter Y or N{Style.reset}\n"
# )
# is used to raise an InnappropriateInput exception imported from classes.exceptions if the wrong input is used when asked
# "Do you wish to delete items? Y/N:".

# KeyError:
#   Key error is a built-in python class that raises an error when an input does not match a key in the dictionary as shown below:
# except KeyError:
# print(
#     f"{Fore.red}Item name not in the list please try again{Style.reset}\n"
# )


def delete_items():
    while True:
        try:
            delete = input("Do you wish to delete items? Y/N:")
            if delete.upper() == "Y":
                saved_combinations = {}
                saved_combo(saved_combinations)
                combo = input("enter name of combo you with to delete: ")
                saved_combinations.pop(combo)
                print(f"{Fore.blue}{saved_combinations}{Style.reset}\n")
                save_and_exit(saved_combinations)
                break
            if delete.upper() != "N":
                # The InnapropriateInput class has been imported from classes.excception and raises an error if the user puts in an inncorrect input.
                raise InappropriateInput(
                    f"{Fore.red}Please enter Y or N{Style.reset}\n"
                )
            break
        except InappropriateInput as e:
            print(e)
        # The KeyError is a builtin python class that raises an error when the input does not match a key in the dictionary, raising an exception that prompts the user to try again.
        except KeyError:
            print(
                f"{Fore.red}Item name not in the list please try again{Style.reset}\n"
            )
