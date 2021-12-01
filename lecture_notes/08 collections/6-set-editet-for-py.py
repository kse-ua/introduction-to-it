ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
print(ages)

ages.append(16);
ages.remove(20);

def printAgeIfInList(*x):
    for i in range(len(x)-1):
        if x[i+1] in x[0]:
            print(x[i+1],": True")
        else:
            print(x[i+1],": False")
printAgeIfInList(ages,10,16,19,20)
ages.clear()
print(ages)
