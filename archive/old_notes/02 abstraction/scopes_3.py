counter = 0


def increment_counter():
    global counter
    counter += 1
    print(f"counter updated! New value: {counter}")
