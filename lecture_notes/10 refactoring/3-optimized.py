import json

def parse(point):
    point = json.loads(point)
    return point

def shift(offset, points):
    for i in range(0, len(points), 1):
        if type(points[i]) == str:
            points[i] = parse(points[i])
        moove(points[i], offset)
    return points

def moove(point,offset):
    point['x'] += offset['x']
    point['y'] += offset['y']

polyline = [
  { "x": 0, "y": 0 },
  { "x": 10, "y": 10 },
  '{ "x": 20, "y": 20 }',
  { "x": 30, "y": 30 },
]

shift({'x': 10, 'y': -5}, polyline)
print(polyline)
