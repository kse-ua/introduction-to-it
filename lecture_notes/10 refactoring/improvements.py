import json

move = lambda dxy:(
  lambda xy:({ 'x': xy['x'] + dxy['dx'], 'y': xy['y'] + dxy['dy'] }))

parsers = {type(''): json.loads, type({}): lambda x:x}

def conditional_parse(item):
  return parsers[type(item)](item)

polyline = [
  {'x': 0, 'y': 0},
  {'x' : 10, 'y' : 10},
  '{"x": 20, "y": 20}',
  {'x': 30, 'y': 30},
]

offset = move({ 'dx': 10, 'dy': -5 })
parsed = map(conditional_parse, polyline)
path = map(offset, parsed)
print(path)
