def addFunction(a, b):
    res = a + b
    return res

cache = {}

def addProcedure(a, b):
    key = a, b
    if key not in cache:
        res = a + b
        cache.update({key:res})
        return res
    else:
        return cache.fromkeys(key)


print([
    addFunction(10, 20),
    addFunction(1, 2),
    addFunction(100, 20),
    addFunction(100, 200),
])

print([
    addProcedure(10, 20),
    addProcedure(1, 2),
    addProcedure(100, 20),
    addProcedure(100, 200),
])
