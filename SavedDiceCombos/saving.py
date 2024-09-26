import json


class NoInput(Exception):
    pass


def __init__(self, name, combo):
    self.name = name
    self.combo = combo


def save_and_exit(saved_combinations):
    json_to_write = []
    json_to_write.append(saved_combinations)
    with open("SavedDiceCombos/saved_combinations.json", "w") as json_file:
        json.dump(json_to_write, json_file, indent=4)


def saved_combo(saving):
    with open("SavedDiceCombos/saved_combinations.json", "r") as json_file:
        json_to_load = json.load(json_file)
        for combo in json_to_load:
            saving.update(combo)


def combo_and_save():
    saved_combinations = {}
    saved_combo(saved_combinations)
    try:
        name = input("Enter the name of your dice combo:\n")
        if not name:
            raise NoInput("input cannot be left empty please provide a name")
    except NoInput as e:
        print("Name cannot be empty please give a name")
        name = input("Enter the name of your dice combo:\n")
    combo = input("Enter the dice combo:\n")
    saved_combinations[name] = combo
    print(saved_combinations)
    save_and_exit(saved_combinations)


# try if n lens = 0 raise exception
