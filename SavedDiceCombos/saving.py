import json
class Saved_Combo:
    def __init__(self, name, combo):
        self.name=name
        self.combo=combo

def save_and_exit():
        json_to_write = []
        json_to_write.append(saved_combinations)
        with open("saved_combinations.json", "w") as json_file:
         json.dump(json_to_write, json_file, indent=4)
def saved_combo(saving):
        with open("saved_combinations.json", "r") as json_file:
            json_to_load = json.load(json_file)
            for combo in json_to_load:
                 saving.update (combo)
                 
saved_combinations = {}
saved_combo(saved_combinations)
name=input("Enter the name of the dice combo:\n")
combo=input("Enter the dice combo:\n")
saved_combinations[name]=combo
print(saved_combinations)
save_and_exit()
