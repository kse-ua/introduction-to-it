import random


def get_int_input():
    while True:
        raw_input = input("Enter number: ")
        if raw_input.isdigit():
            return int(raw_input)
        else:
            print(f"Sorry, '{raw_input}' is not a number")


def congratulate_user():
    print("!!!!!!!!!")
    print("!You won!")
    print("!!!!!!!!!")


def play_game():
    number = random.randint(1, 10)
    user_guessed = False
    while not user_guessed:
        guess = get_int_input()
        if guess == number:
            congratulate_user()
            user_guessed = True


while True:
    play_game()
    want_more = input("Wanna play one more game?")
    if want_more != "Yes":
        quit()
