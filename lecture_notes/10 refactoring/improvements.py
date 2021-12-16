import json

class Shift:
  def __init__(self,offset):
    self.offset = offset

  def move(self,point):
    return {
    'x': point['x'] + self.offset['dx'], 
    'y': point['y'] + self.offset['dy'],
    }

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

shift = Shift({ 'dx': 10, 'dy': -5 })
parsed = map(conditional_parse, polyline)
path = map(lambda point:shift.move(point), parsed)
print(path)
