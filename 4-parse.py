import json


def move(point):
    point['x'] += offset['x']
    point['y'] += offset['y']
    return point

def conditionalParse(point):
    if str(type(point)) == "<class 'dict'>": return point  # type definition, translation to string
    return json.loads(point)


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20,"y": 20}',
    {'x': 30, 'y': 30},
]

print('polyline :', '\n', polyline)
offset = {'x': 10, 'y': -5}
polyline = list(map(conditionalParse, polyline))
path = list(map(move, polyline))
print('path :', '\n', path)
