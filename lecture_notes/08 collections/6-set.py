ages = ({10, 12, 15, 15, 17, 18, 18, 19, 20})
print(ages)

ages.add(16)
ages.remove(20)

print(
  '10:', 10 in ages,
  '16:', 16 in ages,
  '19:', 19 in ages,
  '20:', 20 in ages
)

ages.clear()
print(ages)
