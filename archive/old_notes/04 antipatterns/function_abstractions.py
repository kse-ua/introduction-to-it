import random

min = 1
max = 10




def read_int_input():
    input_is_incorrect = True
    while input_is_incorrect:
        try_input = input(f"Enter a number between {min} and {max}, please")
        if not try_input.isdigit() or int(try_input) < min or int(try_input) >= max:
            continue
        return int(try_input)

def congratulate_player():
    print("---------------------------")
    print("You won!!!!!!!!!!!!!!!!!!!!")
    print("---------------------------")


def play_game(min, max):
    number = random.randint(min, max)
    game_over = False
    while not game_over:
        number_input = read_int_input()

        if number_input == number:
            congratulate_player()
            game_over = True
        else:
            print("Try more")

play_game(3, 4)

file = open("file.txt", "w")
file.re