# Implementation

getFirstAndLast = lambda array: (array[0], array[-1])

# Usage

ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
first, last = getFirstAndLast(ages)
print({first, last})

# So, the python's lambda seems more accurate. However, they both do the same things. In simple words. lambda is a
# func with no name written in one line of code and it may have any number of argm. 
