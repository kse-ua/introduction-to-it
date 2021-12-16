def shift(offset, points):
    for dot in points:
        type_of = type(dot)
        if type_of == dict:
            dot['x'] += offset['x']
            dot['y'] += offset['y']
        else:
            dot.split()
            int((dot[7] + dot[8])) + offset['x']
            int((dot[16] + dot[17])) + offset['y']
    return points


polyline = [{'x': 0, 'y': 0},
            {'x': 10, 'y': 10},
            '{ "x": 20, "y": 20 }',
            {'x': 30, 'y': 30}]


print(shift({'x': 10, 'y': -5}, polyline))
