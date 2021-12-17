import json


type_check = lambda line: json.loads(line) if type(line) != dict else line


shift = lambda point: {"x": point["x"] + offset["x"], "y": point["y"] + offset["y"]}


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
