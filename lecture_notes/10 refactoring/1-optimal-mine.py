import json

def shift(offset, points):
    for point in points:
        type_p = type(point)
        if type_p == dict:
            point['x'] += offset['x']
            point['y'] += offset['y']
        else:
            ind = points.index(point)
            points[ind] = json.loads(point)
            point = points[ind]
            point["x"] += offset['x']
            point["y"] += offset['y']
    return points


polyline = [
  { 'x': 0, 'y': 0 },
  { 'x': 10, 'y': 10 },
  '{ "x": 20, "y": 20 }',
  { 'x': 30, 'y': 30 }
]

print(shift({ 'x': 10, 'y': -5 }, polyline))
