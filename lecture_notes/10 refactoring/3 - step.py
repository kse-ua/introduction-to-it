import json


def shift(coords):
    def move(point):
        point['x'] += coords['x']
        point['y'] += coords['y']
        return point

    return move


def coord_parse(point):
    return point if (type(point) is dict) else json.loads(point)


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]
offset = {'x': 45, 'y': 54}
parsed = list(map(coord_parse, polyline))
path = list(map(shift(offset), parsed))
for obj in path:
    print(obj)
