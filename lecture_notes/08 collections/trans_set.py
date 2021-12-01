ages = {10, 12, 15, 15, 17, 18, 18, 19, 20}
print(ages)

ages.add(16)
ages.remove(20)

def check(x):
  return x in ages

print(f" 10: {check(10)} 16: {check(16)} 19: {check(19)} 20: {check(20)}")

ages.clear()
print(ages)
