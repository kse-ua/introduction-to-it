import json

def shift(offset, points):
    for point in points:
        type_p = type(point)
        if type_p == dict:
            point[x] += offset[x]
            point[y] += offset[y]
        else:
            i = points.index(point)
            points[i] = json.dumps(point)
            #print(point)
            #"""
            point["x"] += offset[x]
            point["y"] += offset[y]
            #"""
    return points

x, y = 0, 0
polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 }
]

print(shift({ x: 10, y: -5 }, polyline))
