import json

def parse(point):
    if str(type(point)) != "<class 'dict'>":
        point = json.loads(point)
    return point

def shift(point, offset):
    point["x"] += offset["x"]
    point["y"] += offset["y"]
    return point

polyline = [
  {"x": 0, "y": 0},
  {"x": 10, "y": 10},
  '{"x": 20, "y": 20}',
  {"x": 30, "y": 30},
]

offset = { "x": 10, "y": -5 }

parsed = list(map(parse, polyline))
shifted = list(map(lambda point: shift( point , offset) , parsed))
print(shifted)
