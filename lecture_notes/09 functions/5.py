cache = {}


def add_procedure(a,b):
    key = f"{a}, {b}"
    if key in cache:
        return cache[key]
    result = a + b
    cache[key] = result
    return result


def sub_procedure(a, b)
    key = f"{a}, {b}"
    if key in cache:
        return cache[key]
    result = a - b
    cache[key] = result
    return result


print({"sub": sub_procedure(5, 2)})
print({"add": sub_procedure(5, 2)})