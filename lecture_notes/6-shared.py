cache = {}

def add_Procedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a - b
    cache[key] = res
    return res

def sub_Procedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a - b
    cache[key] = res
    return res

print('sub:', sub_Procedure(5, 2))
print('sub:', add_Procedure(5, 2))
