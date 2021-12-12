cache_n = {}
def addProcedure(a, b):
    global cache_n
    res = a + b
    cache_n["a + b"] = res
    return res

cache_n = {}
def subProcedure(a, b):
    global cache_n
    res = a - b
    cache_n["a - b"] = res
    return res

print({subProcedure(5, 2)})
print({addProcedure(5, 2)})
