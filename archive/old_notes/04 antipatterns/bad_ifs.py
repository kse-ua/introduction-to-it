def get_age():
    year = input()
    if year.isdigit():
        int_year = int(year)
        if int_year > 1900:
            if int_year <= 2007:
                return 2021 - int_year
            else:
                print("Maximum allowed year is 2007")
                return None
        else:
            print("Sorry, minimum allowed year is 1900")
            return None
    else:
        print("Sorry, enter a year")
        return None
