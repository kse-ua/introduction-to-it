import json

def parse(points):
    for i in range(0, len(points), 1):
        if type(points[i]) == str:
            points[i] = json.loads(points[i])
    return points

def shift(offset, points):
    parse(points)
    for i in range(0, len(points), 1):
        points[i]['x'] += offset['x']
        points[i]['y'] += offset['y']
    return points

polyline = [
  { "x": 0, "y": 0 },
  { "x": 10, "y": 10 },
  '{ "x": 20, "y": 20 }',
  { "x": 30, "y": 30 },
]

shift({'x': 10, 'y': -5}, polyline);
print(polyline)
