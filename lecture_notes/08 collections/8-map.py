dict_of_dicts = {'ages': {
    'Map': {
        # 'Vasia Pupkin': 19,
        # 'Marcus Aurelius': 1860
    }
}}

dict_of_dicts['ages']['Map']['Vasia Pupkin'] = 19
dict_of_dicts['ages']['Map']['Marcus Aurelius'] = 1860
print(dict_of_dicts)

dict_of_dicts['ages']['Map']['Vasia Pupkin'] = 20
print(dict_of_dicts)

dict_of_dicts['ages']['Map'].pop('Vasia Pupkin')
print(dict_of_dicts)

print('Vasia Pupkin:', 'Vasia Pupkin' in dict_of_dicts['ages']['Map'], 
',', 'Marcus Aurelius:', 'Marcus Aurelius' in dict_of_dicts['ages']['Map'])

dict_of_dicts.clear()
print(dict_of_dicts)
