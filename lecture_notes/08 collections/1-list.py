ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

# different functions for REMOVING LAST element:

def removing_using_remove(ages):
    ages = ages.copy()
    ages.remove(20)
    return ages

def removing_del_method(ages):
    ages = ages.copy()
    del ages[-1]
    return ages

def removing_using_pop(ages):
    ages = ages.copy()
    ages.pop(-1)
    return ages

 # different functions for ADDING LAST element:

def adding_using_append(ages):
    ages = ages.copy()
    ages.append(23)
    return ages

def adding_using_extend(ages):
    ages = ages.copy()
    new_list = [27]
    ages.extend(new_list)
    return ages

def adding_using_insert(ages):
    ages = ages.copy()
    ages.insert(9, 77)
    return ages

 # various functions for REMOVING FIRST element:

def deleting_using_remove(ages):
    ages = ages.copy()
    ages.remove(10)
    return ages

def deleting_using_pop(ages):
    ages = ages.copy()
    ages.pop(0)
    return ages

def deleting_del_method(ages):
    ages = ages.copy()
    del ages[0]
    return ages

 # a function for ADDING FIRST element:

def appending_using_insert(ages):
    ages = ages.copy()
    ages.insert(0, 5)
    return ages

def appending_using_slicing(ages):
    ages = ages.copy()
    ages[0:0] = [3]
    return ages


print("Original list:", ages)
print("Removing last element using the:")
print("- 'remove' method:", removing_using_remove(ages))
print("- 'del' method:", removing_del_method(ages))
print("- 'pop' method:", removing_using_pop(ages))
print("Adding last element using the:")
print("~ 'append' function:", adding_using_append(ages))
print("~ 'extend' function:", adding_using_extend(ages))
print("~ 'insert' function:", adding_using_insert(ages))
print("Deleting first element using the:")
print("-- 'remove' method:", deleting_using_remove(ages))
print("-- 'pop' method:", deleting_using_pop(ages))
print("-- 'del' method:", deleting_del_method(ages))
print("We can only add new first element to the list using the:")
print("~~ 'insert' function:", appending_using_insert(ages))
print("~~ or 'slicing' method:", appending_using_slicing(ages))
