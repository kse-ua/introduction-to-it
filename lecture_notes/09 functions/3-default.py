def max(a = 0, b = 0):
    if a > b:
        return a
    return b


print([max(10, 20), max(10), max(-20)])
print([max(b = -20), max(b = 20)])
