import json

def move(offset, points):
    for point in points:
        point['x'] += offset['x']
        point['y'] += offset['y']
    return points


def coditional_parse(item):
    return item if type(item) == dict else json.loads(item)


polyline = [ { 'x': 0, 'y': 0 },
             { 'x': 10, 'y': 10 },
            '{ "x": 20, "y": 20 }',
             { 'x': 30, 'y': 30 } ]

parsed = map(coditional_parse, polyline)
user_input = input('Enter coordinates to move:').split()
path = (move({ 'x': int(user_input[0]), 'y': int(user_input[1]) }, polyline))
print(f'path: \n{list(path)}')
