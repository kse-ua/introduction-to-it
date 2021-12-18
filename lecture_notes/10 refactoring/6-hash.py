import json

def move(o):
    return lambda p: {"x": p["x"] + o["x"], "y": p["y"] + o["y"]}


parsers = {str: json.loads, dict: lambda x: x }


conditionalParse = lambda item: parsers[type(item)](item)

polyline = [
  { "x": 0, "y": 0 },
  { "x": 10, "y": 10 },
  '{ "x": 20, "y": 20 }',
  { "x": 30, "y": 30 }
]

parsed = list(map(conditionalParse, polyline))
path = list(map(move({ 'x': 10, 'y': -5 }), parsed))
print(path)
