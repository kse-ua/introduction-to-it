import json


def parse_shift(points):
    return [json.loads(point) if type(point) == str else point for point in points]


def shift(points, offset):
    for point in points:
        point['x'] += offset['x']
        point['y'] += offset['y']
    
    return points


polyline = [
  { 'x': 0, 'y': 0 },
  { 'x': 10, 'y': 10 },
  '{ "x": 20, "y": 20 }',
  { 'x': 30, 'y': 30 }
]

parser = parse_shift(polyline)
print(shift(parser, {'x': 10, 'y': -5}))