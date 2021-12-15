import ast  # abstract syntax tree, conversion of code "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}

def move(point):
    _type = str(type(point))  # type definition, translation to string
    if _type == "<class 'dict'>":  # python dict = java script object
        point['x'] += offset['x']
        point['y'] += offset['y']
    else:
        point = ast.literal_eval(point)  # returns a dictionary, "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}
        point['x'] += offset['x']
        point['y'] += offset['y']
    return point


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    "{'x': 20,'y': 20}",
    {'x': 30, 'y': 30},
]
print('polyline :', '\n', polyline)
offset = {'x': 10, 'y': -5}
path = list(map(move, polyline))
print('path :', '\n', path)
