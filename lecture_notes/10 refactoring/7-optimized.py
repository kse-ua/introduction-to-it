import ast

def shift(offset, points):
    for point in points:
        point['x'] += offset['x']
        point['y'] += offset['y']
    return points

def parsing(points):
    parsed = []
    for point in points:
        if type(point) == str:
            parsed_point = ast.literal_eval(point)
            parsed.append(parsed_point)
        else:
            parsed.append(point)
    return parsed


polyline = [{'x': 0, 'y': 0},
            {'x': 10, 'y': 10},
            '{ "x": 20, "y": 20 }',
            {'x': 30, 'y': 30}]

parsed_polyline = parsing(polyline)
shifted = shift({'x': 10, 'y': -5}, parsed_polyline)

print(shifted)
