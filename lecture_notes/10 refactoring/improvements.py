import json

move = lambda offset:(
  lambda point:{ 
    'x': point['x'] + offset['dx'], 
    'y': point['y'] + offset['dy']
})

parsers = {
  type(''): json.loads, 
  type({}): lambda dict:dict
}

def conditional_parse(item):
  parser = parsers[type(item)]
  return parser(item)

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
