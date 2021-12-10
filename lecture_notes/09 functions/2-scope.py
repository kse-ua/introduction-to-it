def toLowerCase(cities):
    answearSheat = []
    for item in cities:
        answearSheat.append(item.lower())
    print(answearSheat)
def toUpperCase(cities):
    answearSheat = []
    for item in cities:
        answearSheat.append(item.upper())
    print(answearSheat)
def findLengthOfString(cities):
    answearSheat = []
    for item in cities:
        answearSheat.append(len(item))
    print(answearSheat)
def f1():
    citiesFirst = ['Athens', 'Roma']
    toUpperCase(citiesFirst)
    toLowerCase(citiesFirst)
    citiesSecond = ['London', 'Beijing', 'Kiev']
    toUpperCase(citiesSecond)
#run
cities = ['Athens', 'Roma', 'London', 'Beijing', 'Kiev', 'Riga']
f1()
findLengthOfString(cities)
