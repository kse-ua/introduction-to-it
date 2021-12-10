def addFunction(a, b):
    res = a + b
    return res

cache = {}

def addProcedure (a, b):
    key = str(a) + ", " + str(b)
    res = cache.setdefault(key, None)
    if res != None: 
        return res
    res = a + b
    cache[key] = res
    return res

print([
    addFunction(10, 20),
    addFunction(1, 2),
    addFunction(100, 20),
    addFunction(100, 200)])


print([
    addProcedure(10, 20),
    addProcedure(1, 2),
    addProcedure(100, 20),
    addProcedure(100, 200)])
