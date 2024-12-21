import random

def guess(x): 
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess < random_number:
            print("sorry you guess wrong number it's too low!..")
        elif guess > random_number:
            print("sorry you guess wrong number it's too high!.`.")

    print(f"yeah! Congratulations you have guessed the number {random_number} correctly.")

guess(30)