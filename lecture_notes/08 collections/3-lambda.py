# Implementation

get_first_and_last = lambda array: (array[0], array[-1])

# Usage

ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
first, last = get_first_and_last(ages)
print({'first': first, 'last': last})

# While get_first_and_last lambda in python and getFirstAndLast function in the js version serve the same purpose,
# their return types are not equivalent. The js version returns an object with two properties first and last.
# In the python implementation, a tuple of 2 elements is returned.
