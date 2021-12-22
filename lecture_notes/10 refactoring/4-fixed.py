import json


def shift(offset, points):
    for point in points:
         point['x'] += offset['x']
         point['y'] += offset['y']
    return points



def parser(point):
    if type(point) is dict:
        return point
    return json.loads(point)




polyline = [
    {'x': 0 ,'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]




polyline = list(map(parser, polyline))
shift({'x': 10, 'y': -5}, polyline)
for i in polyline:
    print(i)
