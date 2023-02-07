print("Hello User, Welcome to The Game\nIn this game youll have 5 chances to guess a randomly generated number between 1-100\nWe may drop some hints along the way to make it easier")
import random
ran = random.randint(1,100)
num = 0
"""print("Answer is",ran)"""
while True:
    guess = int(input("Enter your guess: "))
    if guess == ran:
        print("Congratulations! You got it right")
        again=(input("Do you want to play again?\nIf yes enter Y:"))
        if again=="Y":
            continue    
        else:
            break
    elif guess>ran:
        print("Guess a smaller number")
    elif guess<ran:
        print("Guess a bigger number")
    num += 1
    if num == 5:
        ran = random.randint(1,100)
        again=(input("Do you want to play again?\nIf yes enter Y:"))
        if again=="Y":
            continue    
        else:
            break
