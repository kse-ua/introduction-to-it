min_age = 18


def age_is_allowed(years):
    return years >= min_age


age = int(input("Enter your age: "))
if not age_is_allowed(age):
    years_left = 18 - age
    print(f"Please wait {years_left} years more :(")
else:
    print("Welcome!")


