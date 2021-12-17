import json

polyline = [
    {"x": 0, "y": 0},
    {"x": 10, "y": 10},
    '{"x": 20, "y": 20}',
    {"x": 30, "y": 30},
]


def shift(offset, points):
    def moved(point):
        if not isinstance(point, dict):
            point = json.loads(point)

        point["x"] += offset["x"]
        point["y"] += offset["y"]

        return point

    for i in range(len(points)):
        points[i] = map(moved, points[i])

    return points


polyline_new = shift({"x": 10, "y": -5}, polyline)
print(polyline_new)