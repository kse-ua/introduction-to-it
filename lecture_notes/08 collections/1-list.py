ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

ages.append(21)  # Add at the end of array
print(ages)
ages.pop(-1)  # remove at the end of array
print(ages)
ages.insert(0, 9)  # Add at the top of array
print(ages)
ages.pop(0)  # remove at the top of array
print(ages)
<<<<<<< HEAD
print(ages.index(17))


def indexes_of_value(value, values):
    indexes = []
    for i in values:
        if i == value:
            indexes.append(values.index(value))
        values.pop(values.index(value))
    return indexes


print(indexes_of_value(15, ages))
print({'first': first, 'last': last})
print({'first': first, 'last': last})
