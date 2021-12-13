def toLowerCase(cities):
    answearSheat = []
    for item in cities:
        answearSheat.append(item.lower())
    return answearSheat
    
def toUpperCase(cities):
    answearSheat = []
    for item in cities:
        answearSheat.append(item.upper())
    return answearSheat
    
def findLengthOfString(cities):
    answearSheat = []
    for item in cities:
        answearSheat.append(len(item))
    return answearSheat
    
def f1():
    answearList = []
    citiesFirst = ['Athens', 'Roma']
    answearList.append(toUpperCase(citiesFirst))
    answearList.append(toLowerCase(citiesFirst))
    citiesSecond = ['London', 'Beijing', 'Kiev']
    answearList.append(toUpperCase(citiesSecond))
    return answearList
    
#run
cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
answear = f1()
for list in answear:
    print(list)
answear = findLengthOfString(cities)
print(answear)
