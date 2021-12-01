ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

# To add elements in the beginning and at the end of an array
ages.insert(0, 9)
ages.append(21)
# print(ages)

first_after_add = ages[0]
last_after_add = ages[-1]

print({ first_after_add, last_after_add })

# To delete items in the beginning of an array and at the end of it
ages.pop()
ages.pop(0)
# print(ages)
first_after_deletion = ages[0]
last_after_deletion = ages[-1]

print({ first_after_deletion, last_after_deletion })
