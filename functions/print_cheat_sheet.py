from saved.saving import saved_combo
from colored import Fore, Style
from classes.exceptions import InappropriateInput

def print_sheet():
    saved_combinations = {}
    saved_combo(saved_combinations)
    print(f"{Fore.green}{saved_combinations}{Style.reset}\n")


def delete_items():
    while True:
        try:
            delete= input("Do you wish to delete items? Y/N:")
            if delete.upper() == "Y":
             saved_combinations = {}
             saved_combo(saved_combinations)
             saved_combinations.pop(input("enter name of combo you with to delete: "))
             print(f"{Fore.blue}{saved_combinations}{Style.reset}\n")
             break
            if delete.upper() != "N":
                raise InappropriateInput(
                    f"{Fore.red}Please enter Y or N{Style.reset}\n"
                )
            break
        except InappropriateInput as e:
            print(e)  
       
