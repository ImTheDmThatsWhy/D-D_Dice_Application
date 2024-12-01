from saved.saving import saved_combo, save_and_exit
from colored import Fore, Style
from classes.exceptions import InappropriateInput

# This function is designed to delete items in the dictionary. Saved_combinations refers to the json dictionary that contains the items, and saved_combo(saved_combinations) calls the saved dictionary. If the dictionary is empty then an error message would print, else if the items in the dictionary exist then the delete items function will be called. 
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

# This function is designed to print items in the dictionary. Saved_combinations refers to the json dictionary that contains the items, and saved_combo(saved_combinations) calls the saved dictionary. If the dictionary is empty then an error message would print, else the dictionary is printed.
def print_sheet():
    saved_combinations = {}
    saved_combo(saved_combinations)
    if saved_combinations == {}:
        print(
            f"{Fore.red}Dictionary is empty please got to main menu option 3 to create input{Style.reset}\n"
        )
    else:
        print(f"{Fore.green}{saved_combinations}{Style.reset}\n")

# This function deletes items from the existing dictionary, the user is offered the option to delete items and if they select Y for yes then they will be asked to enter the name of the combo they wish to delete. The code is wrapped in a try block so if the user makes an incorrect input an exception is raised. In this function exceptions are raised if a person fails to input a Y or an N when asked, or of they try to select a combo to delete that does not exist in the dictionary.
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
                raise InappropriateInput(
                    f"{Fore.red}Please enter Y or N{Style.reset}\n"
                )
            break
        except InappropriateInput as e:
            print(e)
        except KeyError:
            print(
                f"{Fore.red}Item name not in the list please try again{Style.reset}\n"
            )
