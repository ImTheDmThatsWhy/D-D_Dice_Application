import random
#gives access to randint function to generate random numbers
class Dice:
    def __init__(self, value):
       self.value=value
    def roll(self):
        return random.randint(1,self.value)
def roll_dice():
    valid_dice=["2","4","6","8","10","12","20","100"]
    # while not valid input:
    while True:
        n=input("type the number and type of dice you want eg 2d2, type of dice:d2, d4, d6, d8, d10, d12, d20, and d100:\n")
        n=n.split("d")
        if len(n)<2:
            continue
        if len(n)>3:
            continue
        dice=Dice(int(n[1]))
        number=n[0]
        result=[]
        for i in range(int(number)):
            result.append (dice.roll())
        print(result)
        return result
       
  