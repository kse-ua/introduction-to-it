ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

def listPopFirstNLast(ages_new):
    ages = ages_new.copy()
    for i in range(int(len(ages))//2):
        first = ages[0]
        last = ages[-1]
        print({ first, last })
    
        ages.pop(-1)
        ages.pop(0)
    print(ages)
    return

def listReverseNPop(ages_new):
    ages = ages_new.copy()
    for i in range(len(ages)):
        first = ages[0]
        last = ages[-1]
        print(ages)
    
        ages.pop(-1)
        ages.reverse()
    print(ages)
    return

def listElementsChanges(ages_new):
    ages = ages_new.copy()
    listOfElementsToAdd = [321, 322]
    ages.extend(listOfElementsToAdd)
    ages.insert(4, "mamamia")
    ages.sort
    print(ages)
    ages.pop(4)
    ages.pop(-1)
    ages.remove(321)
    print(ages)

def removeElementFromList(new_list,element):
    a = new_list.count(element)
    print(new_list)
    for i in range(a):
        new_list.remove(element)
        print(new_list)
        
def listCount(ages_new):
    ages = ages_new.copy()
    listOfElementsToAdd = [1234,33,1234,33,1233,33,23]
    ages.extend(listOfElementsToAdd)
    removeElementFromList(ages,1234)
    removeElementFromList(ages,33)
    removeElementFromList(ages,23)
    
listPopFirstNLast(ages)
listReverseNPop(ages)
listElementsChanges(ages)
listCount(ages)
print(ages)
ages.clear()
print(ages)
