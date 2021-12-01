ages = set([10, 12, 15, 17, 18, 18, 19, 20])
print(ages)

ages.add(16)
ages.remove(20)
print(ages)


def includes(element):
    return element in ages


print(includes(10), includes(16), includes(19), includes(20))

ages.clear()
print(ages)
