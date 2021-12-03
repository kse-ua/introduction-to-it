def distinct(dataset):
    directions = list()

    for record in dataset:
        has = (record in directions)
        if not has:
            directions.append(record)

    return directions

# doesn't work with dict-elements unfortunately
def distinct1(dataset):
    return list(set(dataset))


# Usage
flights = [
    {"from": 'Kiev', "to": 'Rome'},
    {"from": 'Kiev', "to": 'Warsaw'},
    {"from": 'Dublin', "to": 'Riga'},
    {"from": 'Riga', "to": 'Dublin'},
    {"from": 'Kiev', "to": 'Rome'},
    {"from": 'Cairo', "to": 'Paris'},
]

filtered = distinct(flights)

for direction in filtered:
    print(direction)
