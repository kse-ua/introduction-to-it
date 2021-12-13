cacheForAdd = {}
cacheForSub = {}

def addProcedure(a, b):
    key = a, b
    if key not in cacheForAdd:
        res = a + b
        cacheForAdd.update({key:res})
        return res
    else:
        return cacheForAdd.fromkeys(key)
def subProcedure(a, b):
    key = a, -b
    if key not in cacheForSub:
        res = a - b
        cacheForSub.update({key:res})
        return res
    else:
        return cacheForSub.fromkeys(key)


print([
    subProcedure(10, 20),
    subProcedure(1, 2),
    subProcedure(100, 20),
    subProcedure(100, 200),
])

print([
    addProcedure(10, 20),
    addProcedure(1, 2),
    addProcedure(100, 20),
    addProcedure(100, 200),
])
