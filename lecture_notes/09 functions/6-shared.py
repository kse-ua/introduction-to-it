cache = {}

def addProcedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a + b
    cache[key] = res
    return res
  
def subProcedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a - b
    cache[key] = res
    return res

print('sub:', subProcedure(5, 2))
print('add:', addProcedure(5, 2))
