def getfromkeys(*names):
    for name in names:
        if name in ages:
            print(name,":",True)
        else:
            print(name,":",False)
ages = {}
print(ages)
ages.update({'Vasia Pupkin': 19})
ages.update({'Marcus Aurelius': 1860})
print(ages)

ages.update({'Vasia Pupkin': 20})
print(ages)

ages.pop('Vasia Pupkin');
print(ages)

getfromkeys('Vasia Pupkin','Marcus Aurelius')

ages.clear();
print(ages)
