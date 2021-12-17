import json


def type_check(line):
    if type(line) != dict:
        return json.loads(line)
    return line


def shift(point):
    point["x"] += offset["x"]
    point["y"] += offset["y"]
    return point


polyline = [
    {"x": 0, "y": 0},
    {"x": 10, "y": 10},
    '{ "x": 20, "y": 20 }',
    {"x": 30, "y": 30},
]

offset = {"x": 10, "y": -5}
checked = list(map(type_check, polyline))
path = list(map(shift, checked))
print(f"polyline: {path}")
