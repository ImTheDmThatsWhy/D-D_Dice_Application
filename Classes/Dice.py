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
        # if(n)[1]!=valid_dice:
        #     continue
        dice=Dice(int(n[1]))
        number=n[0]
        result=[]
        for i in range(int(number)):
            result.append (dice.roll())
        print(result)
        return result
       
    # if n !=2:
    #     continue




    
    


    # def __init__(self, dice, number_of_dice):
    #     dice = input("type in d2, d4, d6, d8, d10, d12, d20, and d100")
    #     if dice == "d2":
    #         print(random.randint(1,2))
    #     elif dice == "d4":
    #         print(random.randint(1,4))
    #     elif dice == "d6":
    #         print(random.randint(1,6))
    #     elif dice == "d8":
    #         print(random.randint(1,8))
    #     elif dice == "d10":
    #         print(random.randint(1,10))
    #     elif dice == "d12":
    #         print(random.randint(1,12))
    #     elif dice == "d20":
    #         print(random.randint(1,20))
    #     elif dice == "d100":
    #         print(random.randint(1,100))
    #     else:
    #         print("Please make a valid selection")

