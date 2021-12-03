arr = [10, 12, 15, 15, 17, 18, 18, 19, 20]
ages = set(arr)
print(ages)

ages.add(16)
ages.remove(20)

print('10:', 10 in ages)
print('16:', 16 in ages)
print('19:', 19 in ages)
print('20:', 20 in ages)

ages.clear()
print(ages)