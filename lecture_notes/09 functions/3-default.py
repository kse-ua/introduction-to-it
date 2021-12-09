# №1
def max(a = 0, b = 0):
    if a > b:
        return a
    else:
        return b

print(maximum(10, 20), maximum(10), maximum(-20))


# №2
max = lambda a = 0, b = 0: a if a > b else b
print(maximum(10, 20), maximum(10), maximum(-20))
