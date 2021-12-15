import json


def move(point):
    if type(point) == str:
        json.loads(point)
    else:
        for key in point:
            if key in offset:
                point[key] = point[key] + offset[key]
            else:
                pass
    return point

polyline = [{ "x": 0, "y": 0 }, { "x": 10, "y": 10 }, 
            '{ "x": 20, "y": 20 }', { "x": 30, "y": 30 }]


offset = move({ "x": 10, "y": -5 })
path = list(map(offset, polyline))
print(path)