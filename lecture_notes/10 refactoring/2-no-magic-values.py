import json


def shift(offset, points, x_key ='x', y_key ='y'):
    for point in points:
        if type(point) is dict:
            point[x_key] += offset[x_key]
            point[y_key] += offset[y_key]
        else:
            index = points.index(point)
            points[index] = json.loads(point)
            points[index][x_key] += offset[x_key]
            points[index][y_key] += offset[y_key]
    return points


polyline = [
    {'x': 0 ,'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]
to_offset = {'x': 10, 'y': -5}
changed = shift(to_offset, polyline)
for obj in changed:
    print(obj)
    
