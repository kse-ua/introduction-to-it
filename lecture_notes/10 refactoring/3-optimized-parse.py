import json


def parse_point(point):
    if type(point) is dict:
        return point
    return json.loads(point)


def shift(offset, points, x_key = 'x', y_key = 'y'):
    for point in points:
        point[x_key] += offset[x_key]
        point[y_key] += offset[y_key]
    return points


polyline = [
    {'x': 0 ,'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]
to_offset = {'x': 10, 'y': -5}
parsed = list(map(parse_point, polyline))
changed = shift(to_offset, parsed)
for obj in changed:
    print(obj)
    
