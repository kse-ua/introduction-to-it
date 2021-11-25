# Python Code:

def getFirstAndLast(array):
    first = ages[0]
    last = ages[-1]

    return first, last


ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
first, last = getFirstAndLast(ages)
print(first, last)

# JS code is pretty the same, however in JS code we can not set "-1" index, as we do in python, thus, we subtract 1 from
# the len of an array. Of course, to print smth in JS we should use .log and semicolon after declaring a var.
# Generally, JS has almost thr same syntax as PY.
