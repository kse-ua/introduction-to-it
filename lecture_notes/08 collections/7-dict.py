ages = {'Vasia Pupkin': 19, 'Marcus Aurelius': 1860}
print(ages)
ages['Vasia Pupkin'] = 20
print(ages)
ages.pop('Vasia Pupkin', 19)
print(ages)


def check_if_true(element):
    if element in ages.keys():
        return True
    else:
        return False

print(check_if_true('Vasia Pupkin'), check_if_true('Marcus Aurelius'))
