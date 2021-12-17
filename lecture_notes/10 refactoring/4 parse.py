import json

polyline = [
    {"x": 0, "y": 0},
    {"x": 10, "y": 10},
    '{"x": 20, "y": 20}',
    {"x": 30, "y": 30},
]


def conditional_parse(item):
    if not isinstance(item, dict):
        item = json.loads(item)

    return item


def move(offset, points):
    for i in range(len(points)):
        points[i] = conditional_parse(points[i])

        points[i]["x"] += offset["x"]
        points[i]["y"] += offset["y"]

    return points


polyline_new = move({"x": 10, "y": -5}, polyline)
print(polyline_new)