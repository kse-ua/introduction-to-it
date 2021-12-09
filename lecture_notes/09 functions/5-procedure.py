def addFunction(a, b):
    res = a + b
    return res

cache = {}

def addProcedure (a, b):
    key = str(a) + ", " + str(b)
    res = 
    if res:
        return res
    res = a + b
    cache[key] = res
    # print(cache)
    return res

addProcedure(3, 4)
addProcedure(1, 2)
addProcedure(100, 20)
addProcedure(100, 200)
