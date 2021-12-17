import json

polyline = [
    {"x": 0, "y": 0},
    {"x": 10, "y": 10},
    '{"x": 20, "y": 20}',
    {"x": 30, "y": 30},
]


def shift(offset, points):
    for i in range(len(points)):
        if not isinstance(points[i], dict):
            points[i] = json.loads(points[i])

        points[i]["x"] += offset["x"]
        points[i]["y"] += offset["y"]

    return points


path=(shift({"x": 10, "y": -5}, polyline))
print(f'path: {path}')