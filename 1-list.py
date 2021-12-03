# Modify example 1-list.* (max grade +10)
# Find in search engine how to add and remove array elements
# Add/remove at the end of array: push, pop
# Add/remove at the top of array: unshift, shift
# Use more array and list methods (see docs) in your examples
# Try to modify and execute examples for JavaScript, Python, and C++

# original program code
# ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
# first = ages[0]
# last = ages[-1]
# print({ 'first': first, 'last': last })

# ----------------------------------------------------------------------------

def _print(str):
    first = ages[0]
    last = ages[-1]
    print('\n'+str)
    print('ages:', ages)
    print('first:', first, ', last:', last)
    return


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

