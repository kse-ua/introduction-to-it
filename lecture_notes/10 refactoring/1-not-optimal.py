import json


def shift(offset, points):
    for point in points:
        types = type(point)
        if types != str:
            point['x'] += offset['x']
            point['y'] += offset['y']
        else:
            i = points.index(point)
            json_string = points[i].replace("'", "\"")
            points[i] = json.loads(json_string)
            points[i]['x'] += offset['x']
            points[i]['y'] += offset['y']

    return points


polyline = [
    { 'x': 0, 'y': 0 },
    { 'x': 10, 'y': 10 },
    '{ "x": 20, "y": 20 }',
    { 'x': 30, 'y': 30 },
]

shift({ 'x': 10, 'y': -5 }, polyline)
print(polyline)
