import json


def PointParse(points):
    return [json.loads(point) if type(point) == str else point for point in points]


def PointsShift(arr, dot_param):
    for dot in arr:
        dot['x'] += dot_param['x']
        dot['y'] += dot_param['y']
    return arr


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    '{ "x": 20, "y": 20 }',
    {'x': 30, 'y': 30},
]

LineIter = PointParse(polyline)

print(PointsShift(LineIter, {'x': 10, 'y': -5}))
