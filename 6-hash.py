import json


move = lambda point: {'x': point['x'] + offset['dx'], 'y': point['y'] + offset['dy']}

parsers = lambda point, x: json.loads(point) if x == True else point

def conditionalParse(point):
    return parsers(point, (str(type(point)) == "<class 'str'>"))


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20,"y": 20}',
    {'x': 30, 'y': 30},
]

print('polyline :', '\n', polyline)
offset = {'dx': 10, 'dy': -5}
polyline = list(map(conditionalParse, polyline))
path = list(map(move, polyline))
print('path :', '\n', path)


