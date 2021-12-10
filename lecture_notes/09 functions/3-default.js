""""
'use strict';

const max = (a = 0, b = 0) => (a > b ? a : b);

console.log([max(10, 20), max(10), max(-20)]);
"""

# ----------------------------------------------------------------------

def max_def_v1(a=0, b=0):
    result = a if a > b else b
    return result


max = max_def_v1
print([max(10, 20), max(10), max(-20)])
