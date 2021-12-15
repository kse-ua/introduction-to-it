import ast  # abstract syntax tree, conversion of code "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}

move = lambda point: {'x': point['x'] + offset['dx'], 'y': point['y'] + offset['dy']}
# other version
# def move(point):
# return {'x': point['x'] + offset['dx'], 'y': point['y'] + offset['dy']}
parsers = lambda point, x: ast.literal_eval(point) if x == True else point
# returns a dictionary, "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}


def conditionalParse(point):
    return parsers(point, (str(type(point)) == "<class 'str'>"))
# other version
#conditionalParse = lambda point: parsers(point, (str(type(point)) == "<class 'str'>"))


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    "{'x': 20,'y': 20}",
    {'x': 30, 'y': 30},
]
print('polyline :', '\n', polyline)
offset = {'dx': 10, 'dy': -5}
polyline = list(map(conditionalParse, polyline))
path = list(map(move, polyline))
print('path :', '\n', path)
