import json


def shift(points, offset):
    for point in points:
        point['x'] += offset['x']
        point['y'] += offset['y']
    return points


def conditional_parse(item):
    if type(item) == dict:
        return item
    return json.loads(item)


polyline = [
  {'x': 0, 'y': 0},
  {'x': 10, 'y': 10},
  '{"x": 20, "y": 20}',
  {'x': 30, 'y': 30},
]

parsed = list(map(conditional_parse, polyline))
print(shift(parsed, {'x': 10, 'y': -5}))
