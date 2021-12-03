# 'use strict';
#// Implementation
# const getFirstAndLast = (array) => ({
#  first: array[0],
#  last: array[array.length - 1],
# });

#const concat = (arr1, arr2) => [...arr1, ...arr2];

#// Usage
# const schoolAges = [10, 12, 15, 15];
# onst studentAges = [17, 18, 18, 19, 20];
# const ages = concat(schoolAges, studentAges);
# const { first, last } = getFirstAndLast(ages);
# console.log({ first, last });

# ---------------------------------------------------------------

# Implementation
getFirstAndLast = lambda array: (array[0], array[-1])

def _print(ages):
    first, last = getFirstAndLast(ages)
    print('\n'+'ages:', ages)
    print('first:', first, ', last:', last)
    return


# Usage
schoolAges = [10, 12, 15, 15]
studentAges = [17, 18, 18, 19, 20]
ages = [*schoolAges,*studentAges]
_print(ages)

# splitting the list using a filter
schoolAges_2 = list(filter(lambda x: x < 17, ages))
_print(schoolAges_2)
studentAges_2 = list(filter(lambda x: x >= 17, ages))
_print(studentAges_2)


