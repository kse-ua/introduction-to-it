def addFunction(a, b):
    res = a + b
    return res

cache = {}

def addProcedure (a, b):
    key = str(a) + ", " + str(b)
    res = cache.update({key})
    if cache.get(key) != 0:
        return res
    res = a + b
    cache[key] = res
    print(cache)
    return res

print(addProcedure(3, 4))
print(addProcedure(3, 4))
