def addFunction(a, b):
    res = a + b
    return res

cache_n = {}
# """
def addProcedure(a, b):
    global cache_n
    """
    key = str(a) + " + " + str(b)
    if type(cache_n[key]) == int:
        return cache_n[key]
    """
    res = a + b
    cache_n["a + b"] = res
    return res


print([addFunction(10, 20),
  addFunction(1, 2),
  addFunction(100, 20),
  addFunction(100, 200)])

print([addProcedure(10, 20),
  addProcedure(1, 2),
  addProcedure(100, 20),
  addProcedure(100, 200)])
"""
d = {'10 +2': 12}
print(d.keys)
"""