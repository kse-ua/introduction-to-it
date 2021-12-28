import json

def shift(offset, points):

    def _shift(point):
        _type = str(type(point))  # type definition, translation to string
        if _type == "<class 'dict'>":  # python dict = javascript object
            point['x'] += offset['x']
            point['y'] += offset['y']
        else:
            point = json.loads(point)
            point['x'] += offset['x']
            point['y'] += offset['y']
        return point

    moved = list(map(_shift, points))

    return moved


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20,"y": 20}',
    {'x': 30, 'y': 30},
]


print('polyline :', '\n', polyline)
path = shift({'x': 10, 'y': -5}, polyline)
print('path :', '\n', path)
