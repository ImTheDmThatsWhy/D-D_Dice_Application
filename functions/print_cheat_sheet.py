from saved.saving import saved_combo
from colored import Fore, Style
def print_sheet():
    saved_combinations = {}
    saved_combo(saved_combinations)
    print(f"{Fore.blue}{saved_combinations}{Style.reset}\n")

       
       