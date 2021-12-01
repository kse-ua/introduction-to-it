ages = dict()

ages['ages'] = {}

ages['ages']['Vasia Pupkin'] = 19
ages['ages']['Marcus Aurelius'] = 1860
print(ages)

ages['ages']['Vasia Pupkin'] = 20
print(ages)

del ages['ages']['Vasia Pupkin']
print(ages)

print(
    'Vasia Pupkin:', 'Vasia Pupkin' in ages['ages'],
    'Marcus Aurelius:', 'Marcus Aurelius' in ages['ages']
)
