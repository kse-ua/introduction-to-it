import ast


def parse(point):
    if type(point) == dict:
        return point
    else:
        return ast.literal_eval(point)


def shift(offset, points):
    modified_points = []
    for point in points:
        arg_type = type(point)
        point = parse(point)
        point['x'] += offset['x']
        point['y'] += offset['y']
        modified_points.append(point)
    return modified_points


polyline = [
    {'x': 0,'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]

results = shift({'x': 10, 'y': -5}, polyline)
print(results)
