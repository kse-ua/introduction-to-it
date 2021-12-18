import json

def move(offset):
    return lambda point: {"x": point["x"] + offset["x"], "y": point["y"] + offset["y"]}


parsers = {
    str: json.loads,
    dict: lambda obj: obj}


def conditionalParse(item):
    parser = parsers[type(item)]
    return parser(item)


polyline = [
  { "x": 0, "y": 0 },
  { "x": 10, "y": 10 },
  '{ "x": 20, "y": 20 }',
  { "x": 30, "y": 30 }
]

parsed = list(map(conditionalParse, polyline))
path = list(map(move({ 'x': 10, 'y': -5 }), parsed))
print(path)
