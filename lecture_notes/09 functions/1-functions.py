def add1(a, b):
    return a + b 


def add_a_b(a, b):
    return a + b
add2 = add_a_b

def add_a_b_new(a, b):
    summ = a + b
    return summ
add3 = add_a_b_new

add4 = lambda a, b: a + b

# print(add1(10, 20))
# print(add2(10, 20))
# print(add3(10, 20))
# print(add4(10, 20))


print({"add1: " : add1(10, 20), "add2: " : add2(10, 20), "add3: " : add3(10, 20), "add4: " : add4(10, 20) })
