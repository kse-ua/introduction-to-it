age = int(input("Enter your age: "))
if age < 18:
    years_left = 18 - age
    print(f"Please wait {years_left} years more :(")
else:
    print("Welcome!")
