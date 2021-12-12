def addFunction(a, b):
    result = a + b
    return result

cache = {}

def addProcedure(a, b):
    key = str(a) + str(b)
    result = cache.setdefault(key, None)
    if result != None:
        return result
    result = a + b
    cache[key] = result
    return result

print(addFunction(10, 20), addFunction(1, 2), addFunction(100, 20), addFunction(100, 200),)

print(addProcedure(10, 20), addProcedure(1, 2), addProcedure(100, 20), addProcedure(100, 200),)
