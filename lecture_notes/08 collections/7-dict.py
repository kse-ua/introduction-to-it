ages = {'Vasia Pupkin': 19, 'Marcus Aurelius': 1860}
print(ages)
ages['Vasia Pupkin'] = 20
print(ages)
ages.pop('Vasia Pupkin', 19)
print(ages)


def includes(element):
   return element in ages.keys()

print(includes('Vasia Pupkin'), includes('Marcus Aurelius'))
