import json


def movePoints(offset, points):
    for point in points:
        if type(point) == str:
            json.loads(point)
        else:
            for key in point:
                if key in offset:
                    point[key] = point[key] + offset[key]
                else:
                    pass
    return points

polyline = [{ "x": 0, "y": 0 }, { "x": 10, "y": 10 }, 
            '{ "x": 20, "y": 20 }', { "x": 30, "y": 30 }]

path = movePoints({ "x": 10, "y": -5 }, polyline)
print(path)