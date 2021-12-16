# Implementation

get_first_and_last = lambda array: (array[0], array[-1])
concat = lambda arr1, arr2: arr1 + arr2

# Usage

schoolAges = [10, 12, 15, 15]
studentAges = [17, 18, 18, 19, 20]
ages = concat(schoolAges, studentAges)
first, last = get_first_and_last(ages)

print({'first': first, 'last': last})
