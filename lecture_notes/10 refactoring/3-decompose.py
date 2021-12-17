import json


def type_check(lines):
    for line in lines:
        if type(line) != dict:
            i = lines.index(line)
            line = json.loads(line)
            lines[i] = line
    return lines


def shift(offset, points):
    for point in points:
        point["x"] += offset["x"]
        point["y"] += offset["y"]
    return points


polyline = [
    {"x": 0, "y": 0},
    {"x": 10, "y": 10},
    '{ "x": 20, "y": 20 }',
    {"x": 30, "y": 30},
]


offset = {"x": 10, "y": -5}
checked = type_check(polyline)
print(shift(offset, checked))
