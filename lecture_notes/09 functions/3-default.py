def fun(a=0, b=0):
    if a > b:
        return a
    else:
        return b


print([fun(10, 20), fun(10), fun(-20)])
