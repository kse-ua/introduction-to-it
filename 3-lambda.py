# Implementation
#getFirstAndLast = lambda array: (array[0], array[-1])

# Usage
# ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
# first, last = getFirstAndLast(ages)
#print({ 'first': first, 'last': last })

# ----------------------------------------------------------------------

# Implementation
getFirstAndLast = lambda array: (array[0], array[-1])

def _print(str):
    first, last = getFirstAndLast(ages)
    print('\n' + str)
    print('ages:', ages)
    print('first:', first, ', last:', last)
    return


# Usage
ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
_print('original list')

ages.append(21)
_print('ages.append(21) - adds an item to the end of the list')
ages.pop()
_print('ages.pop() - removes the item and returns it' + '\n' + 'if no index is specified, the last element is removed')

# python list does not have shift / unshift methods
ages.insert(0,9)
_print('ages.insert(0,9) - inserts an element at the beginning of the list')
ages.pop(0)
_print('ages.pop(0) - removes the first element')



