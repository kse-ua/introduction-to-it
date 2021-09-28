import random

number = random.randint(1, 10)
input_is_incorrect = True
game_over = False

while not game_over:
    number_input = 0
    while input_is_incorrect:
        try_input = input("Enter a number between 1 and 10, please")
        if not try_input.isdigit() or int(try_input) < 1 or int(try_input) >= 10:
            continue
        number_input = int(try_input)
        break

    if number_input == number:
        print("---------------------------")
        print("You won!!!!!!!!!!!!!!!!!!!!")
        print("---------------------------")
    else:
        print("Try more")
