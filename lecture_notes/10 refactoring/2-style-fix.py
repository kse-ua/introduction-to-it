import ast

def shift(offset, points):
    for point in points:
        type_of = type(point)
        if type_of != str:
            point['x'] += offset['x']
            point['y'] += offset['y']
        else:
            i = points.index(point)
            points[i] = ast.literal_eval(point)
            points[i]['x'] += offset['x']
            points[i]['y'] += offset['y']

    return points


polyline = [{'x': 0, 'y': 0},
            {'x': 10, 'y': 10},
            '{ "x": 20, "y": 20 }',
            {'x': 30, 'y': 30}]

shifted = shift({'x': 10, 'y': -5}, polyline)
print(shifted)