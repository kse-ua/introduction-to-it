# 'use strict';
# const ages = {
#   'Vasia Pupkin': 19,
#   'Marcus Aurelius': 1860,
# };
# console.log({ ages });
# ages['Vasia Pupkin'] = 20;
# console.log({ ages });
# Reflect.deleteProperty(ages, 'Vasia Pupkin');
# console.log({ ages });
# console.log({
#   'Vasia Pupkin': Reflect.has(ages, 'Vasia Pupkin'),
#   'Marcus Aurelius': Reflect.has(ages, 'Marcus Aurelius'),
# });

# ---------------------------------------------------------------

ages = {'Vasia Pupkin': 19, 'Marcus Aurelius': 1860}
print('original:', ages)
ages['Vasia Pupkin'] = 20
print('changed age:', ages)
ages.pop('Vasia Pupkin')
print('delete:', ages)

ages_keys = ['Vasia Pupkin', 'Marcus Aurelius']
ages_values = [ages.__contains__(x) for x in ages_keys]
ages_dict = dict(zip(ages_keys, ages_values))
print('check:', ages_keys, '>>', ages_dict)

