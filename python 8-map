_contains = lambda x: ages.__contains__(x)


ages = {'Vasia Pupkin': 19, 'Marcus Aurelius': 1860}
print('original:', ages)
ages['Vasia Pupkin'] = 20
print('changed age:', ages)
ages.pop('Vasia Pupkin')
print('delete:', ages)

ages_keys = ['Vasia Pupkin', 'Marcus Aurelius']
ages_values = map(_contains, ages_keys)
ages_dict = dict(zip(ages_keys, ages_values))
print('check:', ages_keys, '>>', ages_dict)

ages.clear()
print('clear:', ages)
