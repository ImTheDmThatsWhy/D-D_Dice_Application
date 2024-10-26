import json
import re
from colored import Fore, Style
from classes.exceptions import NoInput


def __init__(self, name, combo):
    self.name = name
    self.combo = combo


def save_and_exit(saved_combinations):
    json_to_write = []
    json_to_write.append(saved_combinations)
    with open("saved/saved_combinations.json", "w") as json_file:
        json.dump(json_to_write, json_file, indent=4)


def saved_combo(saving):
    with open("saved/saved_combinations.json", "r") as json_file:
        json_to_load = json.load(json_file)
        for combo in json_to_load:
            saving.update(combo)


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
        correct_combo = re.search("^[1-9]+[0-9]*d([2468]|10|12|20|100)$", combo)
        if correct_combo:
            print(f"{Fore.blue}dice combo accepted{Style.reset}\n")
            break
        else:
            print(
                f"{Fore.red}incorrect please enter a valid D&D dice roll combo eg 3d6{Style.reset}\n"
            )
    saved_combinations[name] = combo
    print(f"{Fore.green}{saved_combinations}{Style.reset}\n")
    save_and_exit(saved_combinations)
