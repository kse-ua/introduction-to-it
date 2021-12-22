import json

def parse(point):
    return json.loads(point) if type(point) == str else point

def moove(point, offset):
    point['x'] += offset['x']
    point['y'] += offset['y']
    return point

def shift(points, offset):
    parsedPoints = list(map(lambda point: parse(point), points))
    moovedPoints = list(map(lambda point: moove(point, offset), parsedPoints))
    return moovedPoints


polyline = [
    {"x": 0, "y": 0},
    {"x": 10, "y": 10},
    '{ "x": 20, "y": 20 }',
    {"x": 30, "y": 30}
]
offset = {'x': 10, 'y': -5}

print(shift(polyline, offset))
