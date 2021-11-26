ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

print({ first, last })
ages.pop(-1)
ages.pop(0) #shift
ages.insert(0, 9) #upshift
ages.append(24)
print(ages)

ages.reverse()
print(ages)
