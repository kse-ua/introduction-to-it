import json


class Shift:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, point, x_key = 'x', y_key = 'y'):
        point[x_key] += self.x
        point[y_key] += self.y
        return point


def parse_point(point):
    return point if (type(point) is dict) else json.loads(point)


polyline = [
    {'x': 0 ,'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]
to_shift = Shift(10, -5)
parsed = list(map(parse_point, polyline))
changed = list(map(to_shift.add, parsed))
for obj in changed:
    print(obj)