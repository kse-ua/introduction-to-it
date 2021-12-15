import json

def move(offset):
  def add_offset_to_point(point):
      point['x'] += offset['x']
      point['y'] += offset['y']
      return point 
  return add_offset_to_point

def conditional_parse(item):
  if type(item) == type({}): 
    return item 
  return json.loads(item)

polyline = [
  {'x': 0, 'y': 0},
  {'x' : 10, 'y' : 10},
  '{"x": 20, "y": 20}',
  {'x': 30, 'y': 30},
]

offset = move({'x':10, 'y':-5 })
parsed = map(conditional_parse, polyline)
path = map(offset, parsed)
print(path)




