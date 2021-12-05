def add1(number_1, number_2):
    return number_1 + number_2


add2 = lambda number_1, number_2: (number_1 + number_2)

print(add1(10, 20), add2(10, 20))
