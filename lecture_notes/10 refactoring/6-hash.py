import json

gen_check = lambda line: type_check(line, type(line) == dict)

type_check = lambda line, x: json.loads(line) if x != True else line

shift = lambda point: {"x": point["x"] + offset["x"], "y": point["y"] + offset["y"]}


polyline = [
    {"x": 0, "y": 0},
    {"x": 10, "y": 10},
    '{ "x": 20, "y": 20 }',
    {"x": 30, "y": 30},
]

offset = {"x": 10, "y": -5}
checked = list(map(gen_check, polyline))
path = list(map(shift, checked))
print(f"polyline: {path}")
