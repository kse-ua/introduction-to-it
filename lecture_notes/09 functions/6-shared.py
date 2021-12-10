cache = {}

def addProcedure (a, b):
    key = str(a) + ", " + str(b)
    res = cache.setdefault(key, None)
    if res != None: 
        return res
    res = a + b
    cache[key] = res
    return res

def subProcedure (a, b):
    key = str(a) + ", " + str(b)
    res = cache.setdefault(key, None)
    if res != None: 
        return res
    res = a - b
    cache[key] = res
    return res

print(f'sub: {subProcedure(5, 2)}')
print(f'add: {addProcedure(5, 2)}')
