# Random is a built-in python class that has been imported so that a random
# number can be returned in the dice class from the range of the given input, as
# shown in the code below:
# def roll_two_dice():
# firstd20 = random.randint(1, 20)

import random

# The colored module has been imported so that the error message can be colored red as demonstrated in the following code:
# raise InappropriateInput(f"{Fore.red}Please enter Y or N{Style.reset}\n"
# The colored module has also been used to color other messages as blue as shown in the code below from the roll dice function:
# n = input(
# f"{Fore.blue}Type the number and type of dice you want eg 2d2, type of dice:d2, d4, d6, d8, d10, d12, d20, and d100:{Style.reset}\n"
# The fore import stylizes the text while style.reset normalizes the text
# The colored module has been used in all functions listed below except roll_two_dice in the same manner as the code
# example above for errors, messages, or results.
from colored import Fore, Style
from classes.dice import Dice
from functions.print_cheat_sheet import print_sheet
from classes.exceptions import InappropriateInput, NegativeError, NonExistantDice


# The cheatsheet function is a function that appears when the user is about to roll a dice that allows the user to view a cheatsheet if they wish.

# Imports and Modules:

# colored: The imported colored functions Fore, and style are used as described above the import from colored code

# Exceptions:
# InnapropriateInput
# The code is wrapped in a try block and the code
# raise InappropriateInput(
# f"{Fore.red}Please enter Y or N{Style.reset}\n"
# )
# is used to raise an InnappropriateInput exception imported from classes.exceptions if the wrong input is used when asked
# ("Do you wish to view cheatsheet? Y/N:")
def cheatsheet():
    while True:
        try:
            cheatsheet = input("Do you wish to view cheatsheet? Y/N:")
            if cheatsheet.upper() == "Y":
                print_sheet()
                break
            if cheatsheet.upper() != "N":
                raise InappropriateInput(
                    f"{Fore.red}Please enter Y or N{Style.reset}\n"
                )
            break
        except InappropriateInput as e:
            print(e)

# This function in summary allows a user to roll any number of a selected valid dice.
# This function also does the following:
# allows users to view a cheatsheet,
# sums the dice if the number of dice is greater then 2,
# allows users to choose to reroll dice.
#
# Imports and Modules:

# Dice: The Dice class has been imported from classes.dice for use in the following code: Dice(int(n[1]))
# Where Dice calls the dice class that has been imported from classes.dice and turns the input n[1]
# (number of faces on the die/dice based on input)into an interger.

# cheatsheet():an imported function that gives players the option to view a cheatsheet.

# colored: The imported colored functions Fore, and style are used as described above the import from colored code

# repeat: Imported so users can repeat the rolldice function (repeat(rolldice)) if they choose to

# Exceptions:
# NonExistantDice: is a class that has been imported from classes.exceptions that raises an exception
# if the input is not not equal to the valid input in the valid dice list as shown below.
# if valid_dice.count(n[1]) == 0:
#     raise NonExistantDice(
#         f"{Fore.red}This dice does not exist pick a valid dice{Style.reset}\n")

# NegativeError is a class that has been imported from classes.exceptions and raises an exception if the user inputs a negative value
# as shown below:
# raise NegativeError(
#     f"{Fore.red}dice number cannot be a negative number{Style.reset}\n"
# )

# ValueError is a built-in python class that raises an exception if the inncorrect value is entered.
# the code below raises an error if the incorrect value has been input and prompts the user to input the correct code
# except ValueError:
#     print(
#         f"{Fore.red}Please input #d# note number input must be >0{Style.reset}\n"
#     )
#     continue
def roll_dice():
    # a list containing the appropriate dice values to select in accordance with Tabletop RPG's like D&D dice values
    valid_dice = ["2", "4", "6", "8", "10", "12", "20", "100"]

    # calls the cheatsheet function which allows users to view saved dice combos before rolling
    cheatsheet()

    while True:
        # asks the user for their input which must follow a #d# format
        n = input(
            f"{Fore.blue}Type the number and type of dice you want eg 2d2, type of dice:d2, d4, d6, d8, d10, d12, d20, and d100:{Style.reset}\n"
        )

        # numbers isolated by splitting based on the d removing the d
        n = n.lower().split("d")
        # if length is less then 2 (length of lists after d is removed) input is incorrect so the user is asked again to input again with the input format specified as #d#

        if len(n) < 2:
            continue
        # If the length is greater then two then the input is still incorrect (length of lists after D is removed)
        if len(n) > 2:
            continue
        try:
            # calls the dice class that has been imported from classes.dice and turns the input (number of faces on the die/dice based on input) into an integer.
            dice = Dice(int(n[1]))
            # turns the number of dice rolls (based on input) into an integer
            number = int(n[0])
            if number < 0:
                # NegativeError is a class that has been imported from classes.exceptions and raises an exception if the user inputs a negative value.
                raise NegativeError(
                    f"{Fore.red}dice number cannot be a negative number{Style.reset}\n"
                )

            # NonExistantDice is a class that has been imported from classes.exceptions that raises an exception if the input is not not equal to the valid input in the valid dice list.
            if valid_dice.count(n[1]) == 0:
                raise NonExistantDice(
                    f"{Fore.red}This dice does not exist pick a valid dice{Style.reset}\n"
                )
            # the resulting dice roll is placed into an empty list
            result = []

            # a random number is generated based on the range specified by the input eg if input is 6 then the number genearted will be randomly selected from 1-6 and the result is appended to the empty list and printed.
            for i in range((number)):

                result.append(dice.roll())
            # if the number of dice rolls is greater then two then the sum of the dice rolls is printed along with the final dice roll.
            if number > 2:
                print(f"Sum of dice = {Fore.blue}{sum(result)}{Style.reset}\n")
            print(f"{Fore.blue}{(result)}{Style.reset}\n")

            # repeat is a function that is called to give the user an option to reroll the dice Y for yes N for No if Y is selected then the roll dice function is repeated.
            repeat(roll_dice)
            break

        # the code below raises an error if the incorrect value has been input and prompts the user to input the correct code
        # ValueError is a built-in python class that raises an exception if the incorrect value is entered.
        except ValueError:
            print(
                f"{Fore.red}Please input #d# note number input must be >0{Style.reset}\n"
            )
            continue
        # raises an error if a user inputs a negative number
        except NegativeError as e:
            print(e)
        # raises an error if the input is incorrect and prompts the user to use the correct input.
        except NonExistantDice as e:
            print(e)


# This function allows a user to repeat a dice roll by asking the user if they want to roll again with Y meaning Yes and N meaning no.
# Imports and modules:

# Exceptions:
# Innappropriate Input: The code is wrapped in a try block so that if the users input is incorrect
# then it raises and inappropriate input error and prompts the user to write the correct input
# as shown below: if roll_again.upper() != "N":
#     raise InappropriateInput(
#         f"{Fore.red}Please enter Y or N{Style.reset}\n"
#     )
# Colored: The imported colored functions Fore, and style are used as described above the import from colored code
def repeat(function_to_repeat):
    while True:
        try:
            roll_again = input("Roll again? Y/N:")
            if roll_again.upper() == "Y":
                function_to_repeat()
                break
            if roll_again.upper() != "N":
                raise InappropriateInput(
                    f"{Fore.red}Please enter Y or N{Style.reset}\n"
                )
            break
        except InappropriateInput as e:
            print(e)


# The roll two dice function rolls two d20 dice and returns two random values to the dice list, the dice list is then sorted from lowest to highest and the resulting list is printed.

# Imports:
# Random: This function uses the built-in python class random
# to generate a random number between 1-20 as shown in the
# code example below:
# firstd20 = random.randint(1, 20)
def roll_two_dice():
    firstd20 = random.randint(1, 20)
    secondd20 = random.randint(1, 20)
    dice_list = [firstd20, secondd20]
    dice_list.sort()
    print(dice_list)
    return dice_list


# The advantage function calls the roll two dice function and prints the highest dice roll in the color blue
# using fore and style functions imported from colored as shown below:
# print("Highest D20 roll is:", f"{Fore.blue}{dice_list[1]}{Style.reset}\n")
# (futher explanation on colored can be found above the from colored code)
# The repeat function is also imported so a user can roll again with advanatge (repeat (advanatage) if they choose to.
def advantage():
    dice_list = roll_two_dice()
    print("Highest D20 roll is:", f"{Fore.blue}{dice_list[1]}{Style.reset}\n")
    repeat(advantage)


# The disadvantage function calls the roll two dice function and prints the lowest dice roll
# in the colour red using fore and style functions imported from colored as shown below:
# print("Lowest D20 roll is:", f"{Fore.red}{dice_list[0]}{Style.reset}\n")
# (futher explanation on colored can be found above the from colored code)
# The repeat function is also imported so a user can roll again with disadvantage (repeat (disadvanatage) if they choose to.
def disadvantage():
    dice_list = roll_two_dice()
    print("Lowest D20 roll is:", f"{Fore.red}{dice_list[0]}{Style.reset}\n")
    repeat(disadvantage)



