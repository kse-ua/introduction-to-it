ages = {
    'Vasia Pupkin': 19,
    'Marcus Aurelius': 1860,
}
print(f'ages: {ages}')

ages['Vasia Pupkin'] = 20
print(f'ages: {ages}')

ages.pop('Vasia Pupkin')
print(f'ages: {ages}')

print({
    'Vasia Pupkin': 'Vasia Pupkin' in ages,
    'Marcus Aurelius': 'Marcus Aurelius' in ages,
})

ages.clear()
print(ages)
