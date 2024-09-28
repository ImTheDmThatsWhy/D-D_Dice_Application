import json
import re


class NoInput(Exception):
    pass
   
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
            name = input("Enter the name of your dice combo:\n")
            if not name:
                raise NoInput("input cannot be left empty please provide a name")
            break
        except NoInput as e:
            print(e)   
    while True:
              combo = input("Enter the dice combo:\n")
              correct_combo=re.search("^[1-9]+[0-9]*d([2468]|10|12|20|100)$",combo)
              if correct_combo:
                 print(" dice combo accepted")
                 break
              else:
                print("incorrect please enter a valid D&D dice roll combo eg 3d6")
    #         combo = input("Enter the dice combo:\n")
    #         if not combo:
    #             raise NoInput("input cannot be left empty please provide a combo")
    #         break
    #     except NoInput as e:
    #         print(e)
    saved_combinations[name] = combo
    print(saved_combinations)
    save_and_exit(saved_combinations)


# try if n lens = 0 raise exception
