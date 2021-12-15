def add_Function(a, b):
    res = a + b
    return res

cache = {}

def add_Procedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a + b
    cache[key] = res
    return res

print([add_Function(10, 20),
       add_Function(1, 2),
       add_Function(100, 20),
       add_Function(100, 200)])

print([add_Procedure(10, 20),
       add_Procedure(1, 2),
       add_Procedure(100, 20),
       add_Procedure(100, 200)])
