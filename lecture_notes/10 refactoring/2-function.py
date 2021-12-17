import json


def shift(offset, points):
    for point in points:
         point['x'] += offset['x']
         point['y'] += offset['y']
    return points


def parser(points):
     for point in points:
          if type(point) is str:
               i = points.index(point)
               points[i] = json.loads(point)
     return points


polyline = [
    {'x': 0 ,'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]

polyline = parser(polyline)
shift({'x': 10, 'y': -5}, polyline)
print(polyline)

