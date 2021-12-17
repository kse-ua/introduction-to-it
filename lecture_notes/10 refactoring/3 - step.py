import json


def move(dots, offset):
    for coord in dots:
        coord['x'] += offset['x']
        coord['y'] += offset['y']
    return dots


def coord_parse(points):
    return [json.loads(point) if type(point) == str else point for point in points]


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    '{ "x": 20, "y": 20 }',
    {'x': 30, 'y': 30},
]

convertion = coord_parse(polyline)

print(move(convertion, {'x': 39, 'y': -100}))
