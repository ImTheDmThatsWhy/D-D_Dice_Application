import random
from colored import Fore, Style
from classes.dice import Dice
from functions.print_cheat_sheet import print_sheet
from classes.exceptions import InappropriateInput, NegativeError,  NonExistantDice

def cheatsheet():
    while True:
        try:
            cheatsheet= input("Do you wish to view cheatsheet? Y/N:")
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

def roll_dice():
    valid_dice = ["2", "4", "6", "8", "10", "12", "20", "100"]
    cheatsheet()
    while True:
        n = input(
            f"{Fore.blue}Type the number and type of dice you want eg 2d2, type of dice:d2, d4, d6, d8, d10, d12, d20, and d100:{Style.reset}\n"
        )
        n = n.split("d")
        if len(n) < 2:
            continue
        if len(n) > 3:
            continue
        try:
            dice = Dice(int(n[1]))
            number = int(n[0])
            if number < 0:
                raise NegativeError(f"{Fore.red}dice number cannot be a negative number{Style.reset}\n")
            if valid_dice.count(n[1]) == 0:
                raise NonExistantDice(
                    f"{Fore.red}This dice does not exist in D&D pick a valid dice{Style.reset}\n"
                )
            result = []
            for i in range((number)):
                result.append(dice.roll())
            if number > 2:
                print(f"Sum of dice = {Fore.blue}{sum(result)}{Style.reset}\n")
            print(f"{Fore.blue}{(result)}{Style.reset}\n")
            repeat(roll_dice)
            break
        except ValueError:
            print(f"{Fore.red}Please input #d# note number input must be >0{Style.reset}\n")
            continue
        except NegativeError as e:
            print(e)
        except NonExistantDice as e:
            print(e)

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

def roll_two_dice():
    firstd20 = random.randint(1, 20)
    secondd20 = random.randint(1, 20)
    dice_list = [firstd20, secondd20]
    dice_list.sort()
    print(dice_list)
    return dice_list

def advantage():
    dice_list = roll_two_dice()
    print("Highest D20 roll is:", f"{Fore.blue}{dice_list[1]}{Style.reset}\n")
    repeat(advantage)

def disadvantage():
    dice_list = roll_two_dice()
    print("Lowest D20 roll is:", f"{Fore.red}{dice_list[0]}{Style.reset}\n")
    repeat(disadvantage)
