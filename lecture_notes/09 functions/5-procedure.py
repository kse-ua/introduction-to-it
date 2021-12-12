def adding_function(a, b):
    res = a + b
    return res

cache = {}

def adding_procedure(a, b):
    key = str(a) + ',' + str(b)
    if key in cache:
        return cache[key]
    res = a + b
    cache[key] = res
    return res

print([adding_function(10, 20), adding_function(1, 2), adding_function(100, 20), adding_function(100, 200)])

print([adding_procedure(10, 20), adding_procedure(1, 2), adding_procedure(100, 20), adding_procedure(100, 200)])
