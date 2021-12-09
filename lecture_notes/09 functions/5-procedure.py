def add_function(a, b):
    result = a + b
    return result

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


print([add_function(10, 20), add_function(1, 2), add_function(100, 20), add_function(100, 200)])
print([add_procedure(10, 20), add_procedure(1, 2), add_procedure(100, 20), add_procedure(100, 200)])
