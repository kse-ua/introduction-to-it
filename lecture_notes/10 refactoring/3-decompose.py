import json

def move(offset):
    def plus(point):
        type_p = type(point)
        if type_p == dict:
            point['x'] += offset['x']
            point['y'] += offset['y']
        else:
            point = json.loads(point)
            point["x"] += offset['x']
            point["y"] += offset['y']
        return point
    path = list(map(plus, polyline))
    return path


polyline = [
  { 'x': 0, 'y': 0 },
  { 'x': 10, 'y': 10 },
  '{ "x": 20, "y": 20 }',
  { 'x': 30, 'y': 30 }
]

print(move({ 'x': 10, 'y': -5 }))
