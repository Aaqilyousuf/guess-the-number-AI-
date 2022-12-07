#Computer is going to think any number we are going to find it
import random

def comp_guess(x):
    computer = random.randint(1,x)
    user = 0
    while user!=computer:
        user = int(input(f"Guess tha number between 1 to {x}: "))
        if user>computer:
            print("Sorry,guess is too high")
        elif user<computer:
            print("Sorry, guess is too low")

    print(f"YAY, you guessed correctly {computer}")

comp_guess(10)

