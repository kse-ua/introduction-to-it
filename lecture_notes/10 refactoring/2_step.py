import json


def move(offset, point):
    if type(point) == dict:
        for key in point:
            if key in offset:
                point[key] += offset[key]
    else:
        point = json.loads(point)
        for key in point:
            if key in offset:
                point[key] += offset[key]
    return point


# that looks not so good, but i don't know how to add 2 arguments to a map function
def mapping(points):
    for i in range(0, len(points)):
        points[i] = move(start_point, points[i])
    return points


polyline = [
    { "x": 0, "y": 0 },
    { "x": 10, "y": 10 },
    '{ "x": 20, "y": 20 }',
    { "x": 30, "y": 30 }]

start_point = { "x": 10, "y": -5 }

path = mapping(polyline)
print(path)

