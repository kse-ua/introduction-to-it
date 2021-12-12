cache = {}

def adding_procedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a + b
    cache[key] = res
    return res


def substracting_procedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a - b
    cache[key] = res
    return res


print('{ sub:', substracting_procedure(5, 2), "}")
print('{ add:', adding_procedure(5, 2), "}")
