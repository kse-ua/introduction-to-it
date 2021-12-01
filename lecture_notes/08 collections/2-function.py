# Python Code:

def getFirstAndLast(array):
    first = ages[0]
    last = ages[-1]

    return first, last


ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
first, last = getFirstAndLast(ages)
print(first, last)
print({ 'first': first, 'last': last })

