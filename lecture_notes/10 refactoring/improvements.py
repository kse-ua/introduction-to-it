import json

move = lambda dxy:(
  lambda xy:({ 'x': xy['x'] + dxy['dx'], 'y': xy['y'] + dxy['dy'] }))
  
def conditionalParse(item):
 return json.loads(item) if type(item) == type('')  else item
   
polyline = [
  {'x': 0, 'y': 0},
  {'x' : 10, 'y' : 10},
  '{"x": 20, "y": 20}',
  {'x': 30, 'y': 30},
]

offset = move({ 'dx': 10, 'dy': -5 })
parsed = map(conditionalParse, polyline)
path = map(offset, parsed)
print(path)
