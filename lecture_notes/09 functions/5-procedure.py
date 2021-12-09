def addfunction(a, b):
    res = a + b
    return res


cache = {}


def addprocedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a + b
    cache[key] = res
    return res


print([
    addfunction(10, 20),
    addfunction(1, 2),
    addfunction(100, 20),
    addfunction(100, 200),
])

print([
    addprocedure(10, 20),
    addprocedure(1, 2),
    addprocedure(100, 20),
    addprocedure(100, 200)
])
