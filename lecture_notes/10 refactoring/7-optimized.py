import ast

def shift(offset, points):
    moved = []
    for point in points:
        moved_x = point['x'] + offset['x']
        moved_y = point['y'] + offset['y']
        moved.append({'x': moved_x, 'y': moved_y})
        
    return moved

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
