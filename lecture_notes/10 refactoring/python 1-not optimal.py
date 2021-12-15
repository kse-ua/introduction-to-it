import ast  # abstract syntax tree, conversion of code "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}

def shift(offset, points):
    for point in points:
        _type = str(type(point))  # type definition, translation to string
        if _type == "<class 'dict'>":  # python dict = java script object
            point['x'] += offset['x']
            point['y'] += offset['y']
        else:
            i = points.index(point)  # defining a list index
            points[i] = ast.literal_eval(point)  # returns a dictionary, "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}
            points[i]['x'] += offset['x']
            points[i]['y'] += offset['y']
    return points


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    "{'x': 20,'y': 20}",
    {'x': 30, 'y': 30},
]
print('polyline :', '\n', polyline)
shift({'x': 10, 'y': -5}, polyline)
print('polyline :', '\n', polyline)
