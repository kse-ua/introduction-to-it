import json

def shift(offset, points):
    for point in points:
        type_of_point = type(point)
        if type_of_point == dict:
            point["x"] += offset["x"]
            point["y"] += offset["y"]
        else:
            i = points.index(point)  # getting the index of that element (here-a string) from points (here-polyline)
            # which is not of dictionary type to convert it from JSON string to Python object
            points[i] = json.loads(points[i]) # converting from JSON string to Python object (dictionary)
            points[i]["x"] += offset["x"]
            points[i]["y"] += offset["y"]
    return points

polyline = [
    {'x': 0 ,'y': 0},
    {'x': 10, 'y': 10},
    '{"x": 20, "y": 20}',
    {'x': 30, 'y': 30}
]

print("polyline: \n", shift({'x': 10, 'y': -5}, polyline))
