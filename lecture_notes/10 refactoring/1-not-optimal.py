import json


def shift(offset, points):
    for point in points:
        arg_type = type(point)
        if arg_type == dict:
            point["x"] += offset['x']
            point['y'] += offset['y']
        if arg_type != dict:
            index = points.index(point)
            points[index] = json.loads(point)
            points[index]['x'] += offset['x']
            points[index]['y'] += offset['y']


polyline = [
    {'x': 0,'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]

shift({'x': 10, 'y': -5}, polyline)
print(polyline)
