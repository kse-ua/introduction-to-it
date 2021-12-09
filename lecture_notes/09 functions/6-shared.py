cache = {}


def addprocedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a + b
    cache[key] = res
    return res


def subprocedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a - b
    cache[key] = res
    return res


print({'sub': subprocedure(5, 2)})
print({'add': addprocedure(5, 2)})
