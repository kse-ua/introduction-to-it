def addFunction(a, b):
    return a + b


cache = {}


def addProcedure(a, b):
    key = f'{a}, {b}'
    res = a + b
    cache[key] = res
    return res


print([
    addFunction(10, 20),
    addFunction(1, 2),
    addFunction(100, 20),
    addFunction(100, 200)
])

print([
    addProcedure(10, 20),
    addProcedure(1, 2),
    addProcedure(100, 20),
    addProcedure(100, 200),
])
