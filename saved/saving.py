import json
import re
from colored import Fore, Style
from classes.exceptions import NoInput

# The JSON class is a built-in python class that has been imported so that dice combos can be saved and loaded from a JSON file
# Regular expressions (re) is a built-in python class that has been imported so that a search pattern could be established for
# the appropriate inputs when creating a dice combo


# This function creates an empty list for combos to be saved into/appended to a json file.
# Imports and Modules:
# json is a built in python module that is being used to save dice combinations in an empty dictionary
# as shown in the code example below:
# save_and_exit(saved_combinations):
# json_to_write = []
# json_to_write.append(saved_combinations)
# with open("saved/saved_combinations.json", "w") as json_file:
#     json.dump(json_to_write, json_file, indent=4)
# where saved_combinations is the name of the json file,
# json_to_write is the empty dictionary
# json_to_write.append(saved_combinations) appends combos
# to the dictionary, with open("saved/saved_combinations.json", "w") as json_file:
# is the location where JSON output is to be stored and json.dump seralizes the
# python object.
def save_and_exit(saved_combinations):
    json_to_write = []
    json_to_write.append(saved_combinations)
    with open("saved/saved_combinations.json", "w") as json_file:
        json.dump(json_to_write, json_file, indent=4)


# This function loads the saved json file using the following code:
# json_to_load = json.load(json_file)
# where json is a built in python module that has been imported.
# while json.load(json) loads the json file into a python dictionary
# with the code for combo in json_to_load adding each combo to the dictionary and then saving it.
def saved_combo(saving):
    with open("saved/saved_combinations.json", "r") as json_file:
        json_to_load = json.load(json_file)
        for combo in json_to_load:
            saving.update(combo)


# This function allows people to put in new combos to save and prompts
# the user for two inputs the first being the name of the combo and the dice combo
# which is then added to the saved_combinations dictionary and saved.

# Imports and modules:

# saved combo(saved_combinations): loads the current json file as a python dictionary

# save_and_exit(saved_combinations): saves the appended saved_combinations list

# Exceptions:
#   NoInput is a class imported from classes.exceptions that raises an exception
#   if the user executes an empty input.

# The colored module has been imported so that the error messages can be colored red
# as demonstrated in the following code example:
#  f"{Fore.red}input cannot be left empty please provide a name{Style.reset}\n"
# The colored module has also been used to color a success messages as shown in the code below:
#    print(f"{Fore.blue}dice combo accepted{Style.reset}\n")
# The fore import stylizes the text while style.reset normalizes the text. The colored module has been used in all functions
# listed below in the same manner as the code example above for error messages and print messages.
def combo_and_save():
    saved_combinations = {}
    saved_combo(saved_combinations)
    while True:
        try:
            name = input("Enter the name of your dice combo:\n").strip()
            if not name:
                raise NoInput(
                    f"{Fore.red}input cannot be left empty please provide a name{Style.reset}\n"
                )
            # I am not putting a regular expression here in case a user wishes to input something like Fireball 4th level or death saves:1.2.3
            break
        except NoInput as e:
            print(e)
    while True:
        combo = input(
            "Enter the dice combo (valid dice are: d2, d4, d6, d8, d10, d12, d20, and d100):\n"
        )
        # this code insures that the dice combination is correct by only allowing specified numbers of 2,4,6,8,10,12,20 and 100 in the format of #d#
        correct_combo = re.search("^[1-9]+[0-9]*d([2468]|10|12|20|100)$", combo)
        if correct_combo:
            print(f"{Fore.blue}dice combo accepted{Style.reset}\n")
            break
        else:
            # if the person inputs the incorrect combo then an the message below will be raised prompting the user to write the correct input
            print(
                f"{Fore.red}incorrect please enter a valid dice roll combo eg 3d6{Style.reset}\n"
            )
    saved_combinations[name] = combo
    print(f"{Fore.green}{saved_combinations}{Style.reset}\n")
    save_and_exit(saved_combinations)
