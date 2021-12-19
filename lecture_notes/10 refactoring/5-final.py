import ast


def parse(point):
    parsing = point if (type(point) == dict) else (ast.literal_eval(point))
    return parsing


def move(offset, point):
    point['x'] += offset['x']
    point['x'] += offset['x']
    return point


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]

parsed = list(map(parse, polyline))
offset = list(map(move({'x': 10, 'y': -5}), parsed))
print(offset)
