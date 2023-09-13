def get_age():
    year = input()
    if not year.isdigit():
        print("Sorry, enter a year")
        return None

    int_year = int(year)
    if int_year <= 1900:
        print("Sorry, minimum allowed year is 1900")
        return None

    if int_year > 2007:
        print("Maximum allowed year is 2007")
        return None

    age = 2021 - int_year