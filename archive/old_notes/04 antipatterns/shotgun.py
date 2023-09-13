def get_age():
    year = int(input())
    current_year = 2022
    if year >= current_year:
        print(f"Sorry, allowed maximum is {current_year}")
        return None

    return current_year - year
