ages = {
  'Vasia Pupkin': 19,
  'Marcus Aurelius': 1860,
}
print(ages)

ages['Vasia Pupkin'] = 20
print(ages)

ages.pop('Vasia Pupkin')
print(ages)

print(
  'Vasia Pupkin' in ages, '\n',
  'Marcus Aurelius' in ages
)
