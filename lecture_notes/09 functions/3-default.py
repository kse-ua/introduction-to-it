def max(x=0, y=0):
    if x > y:
        return x
    elif x < y:
        return y
    elif x == y:
        return x


print(max(10, 20), max(10), max(-20), max())
