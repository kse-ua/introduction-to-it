def get_age():
    year = int(input())
    if year >= 2021:
        print("Sorry, allowed maximum is 2021")
        return None

    return 2021 - year
