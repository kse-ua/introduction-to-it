import json

def shift(offset, points):
    for i in range(0, len(points)):
        typeof = type(points[i])
        if typeof == dict:
            for key in points[i]:
                if key in offset:
                    points[i][key] += offset[key]
        else:
            points[i] = json.loads(points[i])
            for key in points[i]:
                if key in offset:
                    points[i][key] += offset[key]
    return points

polyline = [
    { "x": 0, "y": 0 },
    { "x": 10, "y": 10 },
    '{ "x": 20, "y": 20 }',
    { "x": 30, "y": 30 }]

path = shift({ "x": 10, "y": -5 }, polyline)
print(path)
