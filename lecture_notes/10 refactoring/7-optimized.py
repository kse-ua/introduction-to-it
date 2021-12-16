import ast

def shift(offset, points):
    for point in points:
        point['x'] += offset['x']
        point['y'] += offset['y']
    return points

def parsing(points):
    parsed = [ast.literal_eval(point) if type(point) == str else point for point in points]
    return parsed


polyline = [{'x': 0, 'y': 0},
            {'x': 10, 'y': 10},
            '{ "x": 20, "y": 20 }',
            {'x': 30, 'y': 30}]

parsed_polyline = parsing(polyline)
shifted = shift({'x': 10, 'y': -5}, parsed_polyline)

print(shifted)
