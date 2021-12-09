cache = {}

def add_procedure(a, b):
    key = f"{str(a)}, {str(b)}"
    cache[key] = None
    result = cache[key]
    if result:
        return result
    result = a + b
    cache[key] = result
    return result

def sub_procedure(a, b):
    key = f"{str(a)}, {str(b)}"
    cache[key] = None
    result = cache[key]
    if result:
        return result
    result = a - b
    cache[key] = result
    return result


print(f"sub: {sub_procedure(5, 2)}")
print(f"add: {add_procedure(5, 2)}")
