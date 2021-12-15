cache = {}

def addProcedure(a, b):
    key = f'{a}, {b}'
    res = cache.get[key]
    if res:
        return res
    res = a + b
    cache[key] = res
    return res

def subProcedure(a, b):
    key = f'{a}, {b}'
    res = cache.get[key]
    if res:
        return res
    res = a - b
    cache[key] = res
    return res



print('{', f'sub: {subProcedure(5, 2)}', '}')
print('{', f'add: {addProcedure(5, 2)}', '}')