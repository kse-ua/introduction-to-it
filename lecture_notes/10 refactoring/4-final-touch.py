import json

def element_type(point):
    return point if (type(point) is dict) else json.loads(point)

def shift(offset, points):
    added_points = []
    for point in points:
        point["x"] += offset["x"]
        point["y"] += offset["y"]
        added_points.append(point)
    return added_points

polyline = [ {'x': 0 ,'y': 0}, {'x': 10, 'y': 10}, '{"x": 20, "y": 20}', {'x': 30, 'y': 30} ]
type_of = map(element_type, polyline)
print("polyline: \n", shift({'x': 10, 'y': -5}, type_of))
