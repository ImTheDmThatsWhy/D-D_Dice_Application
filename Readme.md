# Introduction

This dice app will allow players to easily roll D&D dice during a campaign.

## Background: What is D&D:

For people unfamiliar with D&D, D&D stands for dungeons and dragons and is a fantasy table-top role playing game. In the game players form a party and embark on epic quests as they explore a world or worlds together.

## What is the purpose of dice rolls?

In D&D players will use dice rolls for a wide array of features but the main applications can be boiled down to the following:

-Attack rolls (do you succesfully hit a target?)

-Skill checks and saving throws (Involves rolling a 20 sided die the higher you roll the more likely you are to be successful)

-Damage rolls (players are equipped with weapons which depending on what weapon they use will usually require a roll from a d6, d8, d10, or d12 die)

## Imports:

### Black Module

Import black by creating a virtual environment in the terminal (-m venv .venv), then use (source .venv/bin/activate)to activate, then install using (pip install black), to create a list requirements use (pip freeze > requirements.txt). Black will be used to automatically format the files to the pep 8 style which is considered a standard of python. To use the black module to edit the files type

```
black .
```

into the terminal.

### Random Module

Import random to use randint for random number generation. To import just type

```python
import random
```

To generate random numbers use the randint function for example:

```python
def roll_two_dice():
    firstd20 = random.randint(1, 20)
    secondd20 = random.randint(1, 20)
    dice_list = [firstd20, secondd20]
    dice_list.sort()
    print(dice_list)
    return dice_list
```

into the file you plan on using it. In this case it is the Die.py file.

Import color: Like the black module, the color module needs to be installed in a virtual environment the same way as the black import, but with the word black substituted for the word color. The colour module will be used to make the app more reader friendly in the terminal, by coloring outputs and headings. For example the code below colors the output of the highest or lowest roll depending on if a person is rolling with advantage or disadvantage.

```python
def advantage():
    dice_list = roll_two_dice()
    print("Highest D20 roll is:", f"{Fore.blue}{dice_list[1]}{Style.reset}\n")


def disadvantage():
    dice_list = roll_two_dice()
    print("Lowest D20 roll is:", f"{Fore.red}{dice_list[0]}{Style.reset}\n")
```

The output of the code above looks like the following (20 is highlighted blue):

```
Enter your choice:
1
Rolling with advantage
[17, 20]
Highest D20 roll is: 20
```

### Json Module:

The json module has been imported to allow for the user of the app to create a cheat sheet by saving the name and combo of specialised D&D rolls. The json module does not require the creation of a virtual environment or pip install for use, and can be used by writing import json at the top of the file where the coder wants to create a function that saves files.

```python
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
```

## Application Functions:

### Roll Dice

In D&D there as previously mentioned there are specific dice that players roll depending on the situation the dice featured in D&D are the following:
[D2, D4, D6, D8, D9, D10, D12, D20, and D100.]
The roll function allows the app user to select which D&D dice they need and how many they need to roll.
The user also has the option to view a cheat sheet before they roll if they struggle to remember what rolls are needed for certain actions.

## Disadvantage and Advantage Rolls:

In D&D there are often scenarios where a player will be required to roll with disadvantage (lowest roll of two d20) or advantage (highest roll of two d20). This function allows users to roll with advantage or disadvantage, perform rerolls and view there lowest or highest score in the terminal.
