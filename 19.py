import random

while True:
    choice = input("Do you want to collect money? (yes/no):")

    if choice.lower() == "yes":
        dice = random.randint(1,6)
        money = dice*10
        print("Dice rolled:", dice)
        print("You collect money", money)

    else:
        print("Game over!")
        break