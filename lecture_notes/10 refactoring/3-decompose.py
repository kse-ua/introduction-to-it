import json

def move(offset):
    def add_move(point):
        type_1 = type(point)
        if type_1 == type({}):
            point['x'] += offset['x']
            point['y'] += offset['y']
        else:
            point = json.loads(point)
            point['x'] += offset['x']
            point['y'] += offset['y']
        return point 
    return add_move



polyline = [
    { 'x': 0, 'y': 0 },
    { 'x': 10, 'y': 10 },
    '{ "x": 20, "y": 20 }',
    { 'x': 30, 'y': 30 },
]

offset = move({'x':10, 'y':-5 })
path = map(offset, polyline)
print(path)
