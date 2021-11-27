def distinct(dataset):
    distinct_dataset = {}
    for record in dataset:
        key = ''.join((record[key] for key in sorted(record.keys())))
        if key not in distinct_dataset:
            distinct_dataset[key] = dict(record)

    return list(distinct_dataset.values())


flights = [
    {'from': 'Kiev', 'to': 'Rome'},
    {'from': 'Kiev', 'to': 'Warsaw'},
    {'from': 'Dublin', 'to': 'Riga'},
    {'from': 'Riga', 'to': 'Dublin'},
    {'from': 'Kiev', 'to': 'Rome'},
    {'from': 'Cairo', 'to': 'Paris'},
]
print(f'flights: {flights}')

directions = distinct(flights)
print(f'directions: {directions}')
