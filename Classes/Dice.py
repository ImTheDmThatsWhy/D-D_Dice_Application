import random
from colored import Fore, Style


# gives access to randint function to generate random numbers
class NegativeError(Exception):
    pass


class NonExistantDice(Exception):
    pass


class Dice:
    def __init__(self, value):
        self.value = value

    def roll(self):
        return random.randint(1, self.value)


def roll_dice():
    valid_dice = ["2", "4", "6", "8", "10", "12", "20", "100"]
    while True:
        n = input(f"{Fore.blue}Type the number and type of dice you want eg 2d2, type of dice:d2, d4, d6, d8, d10, d12, d20, and d100:{Style.reset}\n")
        n = n.split("d")
        if len(n) < 2:
            continue
        if len(n) > 3:
            continue
        try:
            dice = Dice(int(n[1]))
            number = int(n[0])

            if number < 0:
                raise NegativeError("dice number cannot be a negative number")
            if valid_dice.count(n[1]) == 0:
                raise NonExistantDice(
                    "This dice does not exist in D&D pick a valid dice"
                )
            result = []
            for i in range((number)):
                result.append(dice.roll())
            if number > 2:
                print(f"Sum of dice = {Fore.blue}{sum(result)}{Style.reset}\n")
            print(f"{Fore.blue}{(result)}{Style.reset}\n")
            roll_again=input("Roll again? Y/N:")
            if roll_again=="Y":
                continue
            return result
        except ValueError:
            print("Please input #d# note number input must be >0")
            continue
        except NegativeError as e:
            print("dice number cannot be a negative number")
        except NonExistantDice as e:
            print("This dice does not exist in D&D pick a valid dice")
    
