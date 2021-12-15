def add_procedure(a, b):
    key = f'{str(a)},{str(b)}'
    if key in cache:
        return cache[key]
    result = a + b
    cache[key] = result
    return result

cache = {}
def sub_procedure(a, b):
    key = f'{str(a)},{str(b)}'
    if key in cache:
        return cache[key]
    result = a - b
    cache[key] = result
    return result


print('sub:', sub_procedure(5, 2))
print('add:', add_procedure(5, 2))
