def person_exists(person, cards):
    low = 0
    up = len(cards) - 1
    while low <= up:
        middle = int((low + up) / 2)
        guess = cards[middle]
        if guess == person:
            return True
        if guess > person:
            up = middle - 1
        else:
            low = middle + 1
    return False


catalog = ["A", "B", "C", "D", "E"]
print(person_exists("A", catalog))  # True
print(person_exists("C", catalog))  # True
print(person_exists("F", catalog))  # False
