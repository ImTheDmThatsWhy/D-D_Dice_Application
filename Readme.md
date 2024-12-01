# Set Up

To run the app in VS code please note that if opening in Vs code then Ubuntu 22-.04 (WSL) must be installed
Using VS code:
To set up and run this application a user needs to perform the following steps
-Have python3 installed
(for windows use the instructions from the following website https://learn.microsoft.com/en-us/windows/python/beginners)

-   Next clone the code from Github by going to the link below https://github.com/ImTheDmThatsWhy/D-D_Dice_Application and click on the code button and click copy code, then in VS code click on the search bar at the top and type >Git:Clone (or go to show and run commands and search for Git:Clone and click on it) then paste the copied code into the search bar it will then prompt you to save the cloned repository to a folder

-   After you have saved the repository open the folder in VS code by clicking on file open folder,

-   After you have opened the folder, open up a terminal by clicking on terminal then new terminal and open up to the Ubuntu 22.04 (WSL),

-   Once the terminal is open type python3 main.py to run the app.

# Introduction

This dice app will allow players to easily roll D&D dice during a campaign.

## Background: What is D&D:

For people unfamiliar with D&D, D&D stands for Dungeons and Dragons and is a fantasy table-top role playing game. In the game players form a party and embark on epic quests as they explore a world or worlds together.

## What is the purpose of dice rolls?

In D&D players will use dice rolls for a wide array of features but the main applications can be boiled down to the following:

-Attack rolls (do you succesfully hit a target?)

-Skill checks and saving throws (Involves rolling a 20 sided die the higher you roll the more likely you are to be successful)

-Damage rolls (players are equipped with weapons which depending on what weapon they use will usually require a roll from a d6, d8, d10, or d12 die)

## Imports:

### Black Module

Import black by creating a virtual environment in the terminal (-m venv .venv), then use (source .venv/bin/activate) to activate, then install using (pip install black), to create a list requirements use (pip freeze > requirements.txt). Black will be used to automatically format the files to the pep 8 style which is considered a standard of python. To use the black module to edit the files type

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

### Colored Module

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

### Re module:

The regular expressions module does not require a virtual environment or pip to be used and can simply be imported by writing

```python
import Re
```

into the file where the module is intended to be used. In this application it has been used to check that the specified regular expressions are in a string.

## Application Functions:

### Roll Dice

In D&D there as previously mentioned there are specific dice that players roll depending on the situation the dice featured in D&D are the following:
[d2, d4, d6, d8, d10, d12, d20, and d100.]
The roll function allows the app user to select which D&D dice they need and how many they need to roll.
The user also has the option to view a cheat sheet before they roll if they struggle to remember what rolls are needed for certain actions.

## Disadvantage and Advantage Rolls:

In D&D there are often scenarios where a player will be required to roll with disadvantage (lowest roll of two d20) or advantage (highest roll of two d20). This function allows users to roll with advantage or disadvantage, perform rerolls, and view their lowest or highest score in the terminal.

## Create dice combinations:

In this menu option the user is prompted to name and create a dice combination that they can view before rolling later, in case they have forgotten the specifics of dice rolls required for certain attacks or skills.

## View and edit saved dice combinations:

Allows the user to view their saved combos and delete combos

## Future functions

In the future this app plans to implement the following:

-   Allow users to use their saved combos to roll
-   Create a dice table so that the user can roll a random item
-   Add the users modifiers to a roll

## Licensing and Dependancies:

### MIT LICENSE:

```
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

### Colored module:

The colored module has the following relevant information:

Author: Dimitris Zlantanidis

Requirements: Python>=3.9 (requires version 3.9 or higher)

License: Mit Approved license:

In accordance with information found on open source intiative (https://opensource.org/license/mit), the Mit License means that permission is granted free of charge to any person who has a copy of the software. Furthermore, the software can be used without restriction and the user can use, copy, modify, merge, publish, distribute, and sell copies of the software unrestrictedly provided that the user also notes that aoftware in question (colored) is under the MIT license. As this is an open license there is no ethical concerns about the use of color is this application as I have acknowledged that colored is under the MIT license.

Environment: Console

Operating Systems:

-   Microsoft Windows

-   Microsoft Windows Windows 10

-   OS Independent

-   POSIX Linux

-   POSIX Other

### Black Module:

The Black module has the following relevant information:

Author: Łukasz Langa

Requirements: Python>=3.8 (requires version 3.8 or higher)

License: Mit Approved license: No concerns in terms of ethics (see the mit license information in colored for more information)

Environment: Console

Operating System: Os independant it works on any operating system.

### Module already in python (Re, JSON, Random):

As these module are a part of python 3 the assumption is being made that they follow the license for python.

License for python PSF:
According to https://docs.python.org/3/license.html there are no ethical concerns because python software is not bundled with this appication. Therefore, there has been no breach to the terms of the license.

### Dependecies:

For black and color modules all additional dependencies required can be found in the requirements.txt file of this application.
