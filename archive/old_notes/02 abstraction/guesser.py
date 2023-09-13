import random


number = random.randint(1, 10)
user_guessed = False
while not user_guessed:
    guess = int(input(f"Enter number: "))
    if guess == number:
        print("You won!")
        user_guessed = True
