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

Import black by creating a virtual environment in the terminal (-m venv .venv), then use (source .venv/bin/activate)to activate, then install using (pip install black), to create a list requirements use (pip freeze > requirements.txt). Black will be used to automatically format the files to the pep 8 style which is considered a standard of python

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

Import color: same way as the black import but substitute the word black for the word color. The colour module will be used to make the app more reader friendly in the terminal, by coloring outputs and headings. For example the code below colors the output of the highest or lowest roll depending on if a person is rolling with advantage or disadvantage.

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

##
