import json


def parse_point(point):
    return point if (type(point) is dict) else json.loads(point)


def shift(offset, x_key = 'x', y_key = 'y'):
    def add(point):
        point[x_key] += offset[x_key]
        point[y_key] += offset[y_key]
        return point
    return add


polyline = [
    {'x': 0 ,'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]
to_offset = {'x': 10, 'y': -5}
result = list(map(parse_point, polyline))
changed = list(map(shift(to_offset), result))
for obj in changed:
    print(obj)
    
