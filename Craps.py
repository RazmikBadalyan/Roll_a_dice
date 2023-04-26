import random

def roll_dice():
    return random.randint(1, 6)

diceThrow1 = roll_dice()
diceThrow2 = roll_dice()
answer = diceThrow1 + diceThrow2

print(f"The sum of dice is {diceThrow1} + {diceThrow2} = {answer}")

if answer in (7, 11):
    print("You win!")
elif answer in (2, 3, 12):
    print("You lose")
else:
    print(f"Now your goal number is {answer}")
    while True:
        diceThrow1 = roll_dice()
        diceThrow2 = roll_dice()
        answer1 = diceThrow1 + diceThrow2
        print(f"The sum of dice is {diceThrow1} + {diceThrow2} = {answer1}")
        if answer1 == 7:
            print("You lose((")
            break
        elif answer1 == answer:
            print("You win!")
            break
