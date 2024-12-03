# The random module has been imported so that a random number be returned in the dice class from the range of the given input for example if the input is 6, then the random.randomint will return a random interger between 1-6.
import random

# The colored module has been imported so that error messages can be colored red the fore colours the text and Style.reset normalizes the text.It is also used for the advantage function to color the highest dice roll blue, and in the disadvanatge function the color red
from colored import Fore, Style
from classes.dice import Dice
from functions.print_cheat_sheet import print_sheet
from classes.exceptions import InappropriateInput, NegativeError, NonExistantDice


# the cheatsheet function is a function that appears when the user is about to roll a dice that allows the user to view a cheatsheet if they wish. The user is asked to input a Y for yes or N for no. If the user selects yes then the cheat sheet is printed and the loop breaks. The code is wrapped in a try block so that if the user incorrectly inputs something other then Y or N then an innapropriate input error is raised.The InnapropriateInput class has been imported from Classes.excceptions.
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

    # This function is summary allows a user to roll any number of a selected D&D dice in addition the roll die function allows the following:
    # - gives users an option to view a cheat sheet containing saved dice combos
    # - performs of sum of the dice values rolled if the number rolled is >3
    # - gives users the option to reroll dice and select a new input.


def roll_dice():
    # a list containing the appropriate dice values to select in accordance with D&D dice values
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
            # calls the dice class that has been imported from classes.dice and turns the input (number of faces on the die/dice based on input)into an interger.
            dice = Dice(int(n[1]))
            # turns the number of dice rolls (based on input) into an interger
            number = int(n[0])
            if number < 0:
                # Negative error is a class that has been imported from Classes.exceptions and raises an exception if the user inputs a negative value.
                raise NegativeError(
                    f"{Fore.red}dice number cannot be a negative number{Style.reset}\n"
                )

            # NonExistantDice is a class that has been imported from Classes.exceptions that raises an exception if the input is not not equal to the valid input in the valid dice list.
            if valid_dice.count(n[1]) == 0:
                raise NonExistantDice(
                    f"{Fore.red}This dice does not exist in D&D pick a valid dice{Style.reset}\n"
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
        # ValueError is a built in class that raises an exception if the inncorrect value is entered.
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


# this function allows a user to repeat a dice roll by asking the user if they want to roll again with Y meaning Yes and N meaning no. The code is wrapped in a try block so that if the users input is incorrec then it raises and inappropriate input error and prompts the user to write the correct input.
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
def roll_two_dice():
    firstd20 = random.randint(1, 20)
    secondd20 = random.randint(1, 20)
    dice_list = [firstd20, secondd20]
    dice_list.sort()
    print(dice_list)
    return dice_list


# The advantage function calls the roll two dice function and prints the highest dice roll in the colour blue. The repeat function is also called to prompt a user if they want to roll again if Y for yes is selected then the advantage function is repeated.
def advantage():
    dice_list = roll_two_dice()
    print("Highest D20 roll is:", f"{Fore.blue}{dice_list[1]}{Style.reset}\n")
    repeat(advantage)


# The disadvantage function calls the roll two dice function and prints the lowest dice roll in the colour red. The repeat function is also called to prompt a user if they want to roll again if Y for yes is selected then the disadvantage function is repeated.
def disadvantage():
    dice_list = roll_two_dice()
    print("Lowest D20 roll is:", f"{Fore.red}{dice_list[0]}{Style.reset}\n")
    repeat(disadvantage)
