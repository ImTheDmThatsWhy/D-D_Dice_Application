from Classes.Dice import roll_dice
def dice_combination_menu():
    print ("Enter 1 to roll a saved dice combination")
    print("Enter 2 to proceed to roll dice menu")
    print("Enter 3 to exit")
    choice = input("Enter your answer:\n")

choice=""
while choice!="3":
    if choice =="1":
        print("Enter the name of the saved combination you wish to roll eg fireball")
    elif choice == "2":
        print("Proceeding to dice rolling menu")
        roll_dice()
    elif choice == "3":
        print("Exiting to main menu")
    else:
        print("Invalid input please try again")