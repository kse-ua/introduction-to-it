import json

parse = lambda point: json.loads(point) if(type(point) != dict) else None

def move(offset, point):
    for key in point:
        if key in offset:
            moved =  point[key] + offset[key]
    return moved
    

def mapping(points):
    mapped = []
    for i in range(0, len(points)):
        mapped[i] = move(start_point, points[i])
    return mapped


polyline = [
    { "x": 0, "y": 0 },
    { "x": 10, "y": 10 },
    '{ "x": 20, "y": 20 }',
    { "x": 30, "y": 30 }]

start_point = { "x": 10, "y": -5 }
parsed = list(map(parse, polyline))
path = mapping(parsed)
print(path)
