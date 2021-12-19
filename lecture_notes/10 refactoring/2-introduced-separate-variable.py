import json


def shift(offset, points):
    modified_points = points.copy()
    for point in modified_points:
        arg_type = type(point)
        if arg_type == dict:
            point["x"] += offset['x']
            point['y'] += offset['y']
        else:
            index = modified_points.index(point)
            modified_points[index] = json.loads(point)
            modified_points[index]['x'] += offset['x']
            modified_points[index]['y'] += offset['y']
    return modified_points


polyline = [
    {'x': 0,'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]

results = shift({'x': 10, 'y': -5}, polyline)
print(results)

