# Implementation

def getFirstAndLast(ages):
  first = ages[0]
  last = ages[-1]
  return first, last

# Usage

ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
first, last = getFirstAndLast(ages)
print({ 'first': first, 'last': last })

