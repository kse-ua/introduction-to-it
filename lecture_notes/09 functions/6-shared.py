cache_n = {}
def addProcedure(a, b):
    global cache_n
    key = f"{a} + {b}"
    if key in cache_n:
        return cache_n[key]
    res = a + b
    cache_n[key] = res
    return res

cache_n = {}
def subProcedure(a, b):
    global cache_n
    key = f"{a} - {b}"
    if key in cache_n:
        return cache_n[key]
    res = a - b
    cache_n[key] = res
    return res

print({subProcedure(5, 2)})
print({addProcedure(5, 2)})
print(cache_n)
print({subProcedure(8, 2)})
print(cache_n)
