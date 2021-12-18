import json

 
def shift(offset, points):
   def add_offset_to_point(point):
     type1 = type(point)
     if type1 == type({}):
       point['x'] += offset['x']
       point['y'] += offset['y']
     else:
       point = json.loads(point)
       point['x'] += offset['x']
       point['y'] += offset['y']
     return point 
   moved = map(add_offset_to_point, points)

   return moved 


polyline = [
   {'x': 0, 'y': 0},
   {'x': 30, 'y': 30},
 ]

path = shift({'x':10, 'y':-5 }, polyline)
print(path)
