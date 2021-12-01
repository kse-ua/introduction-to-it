list_of_ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
ages = set(list_of_ages)
print(ages)

ages.add(16)
ages.remove(20)

print(
    "10: " + str(10 in ages) + '\n',
    "16: " + str(16 in ages) + '\n',
    "19: " + str(19 in ages) + '\n',
    "20: " + str(20 in ages)
)

ages.clear()
print(ages)
