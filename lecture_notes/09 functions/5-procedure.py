def add_procedure(a, b):
     cache = {}
     key = str(a) + ', ' + str(b)
     if key in cache:
         return cache[key]
     res = a + b
     cache[key] = res
     return res


 def sub_procedure(a, b):
     cache = {}
     key = str(a) + ', ' + str(b)
     if key in cache:
         return cache[key]
     res = a - b
     cache[key] = res
     return res


 print(add_procedure(5, 2))
 print(sub_procedure(5, 2))