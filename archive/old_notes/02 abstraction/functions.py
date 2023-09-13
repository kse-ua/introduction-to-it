# This is a pure function
def square(x):
    return x * x


# Next functions are functions with side effects
counter = 1


def increment_counter():
    global counter
    counter += 1


def cube(x):
    print(f"calculating cube of {x}")
    return x ** 3
