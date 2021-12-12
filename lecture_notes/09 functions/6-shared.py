cache = {}

def addProcedure(a, b):
    key = str(a) + str(b)
    result = cache.setdefault(key, None)
    if result != None:
        return result
    result = a + b
    cache[key] = result
    return result

def subProcedure(a, b):
    key = str(a) + str(b)
    result = cache.setdefault(key, None)
    if result != None:
        return result
    result = a - b
    cache[key] = result
    return result

print(f'subProcedure: {subProcedure(5, 2)}')

print(f'addProcedure: {addProcedure(5, 2)}')
