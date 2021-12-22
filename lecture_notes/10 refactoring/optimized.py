import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    parsers = {
        str.__name__: json.loads,
        dict.__name__: lambda obj: obj.copy()
    }

    @classmethod
    def parse(cls, obj):
        obj_type = type(obj).__name__
        parser = Point.parsers[obj_type]
        parsed_point = parser(obj)

        return Point(**parsed_point)

    def move(self, offset):
        x = self.x + offset['dx']
        y = self.y + offset['dy']

        return Point(x, y)

    def __str__(self):
        return str({
            'x': self.x,
            'y': self.y
        })

    __repr__ = __str__


offset = {'dx': 10, 'dy': -5}
raw_data = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    '{ "x": 20, "y": 20 }',
    {'x': 30, 'y': 30},
]
polyline = list(map(Point.parse, raw_data))
path = list(map(lambda point: point.move(offset), polyline))
print(path)
