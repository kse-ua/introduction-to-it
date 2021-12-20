import json

def parse(point):
    if type(point) != dict:
        point = json.loads(point)
    else:
        pass
    return point


def move(offset, point):
    for key in point:
        if key in offset:
            point[key] = point[key] + offset[key]
    path = {**point, **offset}
    return path
    

polyline = [
    { "x": 0, "y": 0 },
    { "x": 10, "y": 10 },
    '{ "x": 20, "y": 20 }',
    { "x": 30, "y": 30 }]

start_point = { "x": 10, "y": -5 }
parsed = list(map(parse, polyline))
path = list(map(move, start_point, parsed))
print(path)
