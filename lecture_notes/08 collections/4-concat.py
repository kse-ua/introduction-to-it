# Implementation

get_first_and_last = lambda array: (array[0], array[-1])
concat = lambda arr1, arr2: arr1 + arr2

# Usage
school_ages = [10, 12, 15, 15]
student_ages = [17, 18, 18, 19, 20]
ages = concat(school_ages, student_ages)
first, last = get_first_and_last(ages)
print({ first, last })
