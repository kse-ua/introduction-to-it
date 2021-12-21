import json

def move(offset):
    def plus(point):
        point["x"] += offset["x"]
        point["y"] += offset["y"]
        return point
    return plus
    

def conditionalParse(item):
  if type(item) == dict: return item
  return json.loads(item)


polyline = [
  { "x": 0, "y": 0 },
  { "x": 10, "y": 10 },
  '{ "x": 20, "y": 20 }',
  { "x": 30, "y": 30 }
]

parsed = list(map(conditionalParse, polyline))
path = list(map(move({ 'x': 10, 'y': -5 }), parsed))
print(path)