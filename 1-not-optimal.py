def addFunction(a, b):
    res = a + b
    return res


cache = {}  # dictionary


def addProcedure(a, b):
    key = str(a) + ',' + str(b)
    res = cache
    if res == {}:
         res = cache.fromkeys(key)
    if res.get(key) != None:
        return res.get(key)  # returns the value of the key, but if there is none, then None
    res = a + b
    cache[key] = res
    return res


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
