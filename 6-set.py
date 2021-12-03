ages = {10, 12, 15, 15, 17, 18, 18, 19, 20]}
print(ages)

ages.add(16)
ages.discard(20)

print(f"10:{10 in ages},\n16:{16 in ages},\n19:{19 in ages},\n20:{20 in ages}")

ages.clear()

print(ages)
