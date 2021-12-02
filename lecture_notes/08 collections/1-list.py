ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

new_element = int(input("Enter new last element:"))
ages.append(new_element)
new_element = int(input("Enter new first element:"))
ages.insert(0, new_element)
ind_to_del = int(input("Enter what element to delete:"))
ages.pop(ind_to_del)

first = ages[0]
last = ages[-1]
new_element = int(input())
ages.append(new_element)

print({ 'first': first, 'last': last })
