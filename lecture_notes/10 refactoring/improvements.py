import json

def move(offset):
  def move_to_offset(point):
    type_ = type(point)
    if type_ == type({}):
      point['x'] += offset['x']
      point['y'] += offset['y']
    else:
      point = json.loads(point)
      point['x'] += offset['x']
      point['y'] += offset['y']
    return point
  return move_to_offset


polyline=[
  {'x': 0, 'y': 0},
  {'x' : 10, 'y' : 10},
  '{"x": 20, "y": 20}',
  {'x': 30, 'y': 30},
]

offset = move({'x':10, 'y':-5 })
path = map(offset, polyline)
print(path)


