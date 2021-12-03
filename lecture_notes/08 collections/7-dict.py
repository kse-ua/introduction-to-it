ages = {'Vasia Pupkin': 19, 'Marcus Aurelius': 1860}
print(ages)
ages['Vasia Pupkin'] = 100
print(ages)
ages.pop('Vasia Pupkin', 19)
print(ages)


def includes(element):
    if element in ages.keys():
        return True
    else:
        return False

print(includes('Vasia Pupkin'), includes('Marcus Aurelius'))
