ages = {}

ages['Vasia Pupkin'] = 19
ages['Marcus Aurelius'] = 1860
print({'ages': ages})

ages['Vasia Pupkin'] = 20
print({'ages': ages})

ages.pop('Vasia Pupkin')
print({'ages': ages})

print('Vasia Pupkin:', 'Vasia Pupkin' in ages, "  " 'Marcus Aurelius:', 'Marcus Aurelius' in ages)

ages = {}
print({'ages': ages})
