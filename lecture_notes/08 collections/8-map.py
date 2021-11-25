nested_dict = {'ages': {
    'Map': {
        'Vasia Pupkin': 19,
        'Marcus Aurelius': 1860
    }
}}

print(nested_dict)

nested_dict['ages']['Map']['Vasia Pupkin'] = 20
print(nested_dict)
del nested_dict['ages']['Map']['Vasia Pupkin']

print(nested_dict)

print('Vasia Pupkin:', 'Vasia Pupkin' in nested_dict['ages']['Map'], 'Marcus Aurelius:', 'Marcus Aurelius' in nested_dict['ages']['Map'])

nested_dict.clear()
print(nested_dict)
