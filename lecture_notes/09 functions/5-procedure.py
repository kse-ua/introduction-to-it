def addFunction(a, b):
    res = a + b
    return res


cache = {}  # dictionary


def addProcedure(a, b):
    key = str(a) + ',' + str(b)
    if cache == {}:
        res = cache.fromkeys(key)  # create a dictionary with a key
    else:
        res = cache
    if res.get(key[0]) != None:
        return res.get(key[0])  # returns the value of the key, but if there is none, then None
    res = a + b
    cache[key[0]] = res
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
