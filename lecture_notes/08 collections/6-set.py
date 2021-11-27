ages = {10, 12, 15, 15, 17, 18, 18, 19, 20}
print(f'ages: set({len(ages)}) {ages}')

ages.add(16)
ages.remove(20)
print({n: n in ages for n in (10, 16, 19, 20)})

ages.clear()
print(f'ages: set({len(ages)}) {ages}')
