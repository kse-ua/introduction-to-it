ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

first = ages[0]
last = ages[-1]

print({"first": first, "last": last})

# Remove using pop(index) method
ages.pop(0)

# Remove using remove(value) method
ages.remove(20)

# Add to the beginning
ages.insert(0, 4)

# Add to the end
ages.append(25)

print("The new list is:", ages)
