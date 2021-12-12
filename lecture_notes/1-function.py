from typing import Final

a = 10
b = 20

def add1(a, b):
    return a + b
print(add1(10,20))

add2: Final = a + b

print(add2)

add3: Final = lambda a, b : a + b

print(add3(10,20))

add4: Final = lambda a, b : a + b

print(add4(10,20))
