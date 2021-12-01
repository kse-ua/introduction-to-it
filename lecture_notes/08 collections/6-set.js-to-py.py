ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
print(ages)

ages.insert(5, 16)
ages.pop()

print(
    10 in ages,
    16 in ages,
    19 in ages,
    20 in ages,
)

ages.clear()
print(ages)
