import ast  # abstract syntax tree, conversion to code "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}


class Shift:
    def __init__(self, offset):  # python __init__ = javascript constructor
        self.offset = offset  # python self = javascript this

    def move(self, point):
        dx = list(self.offset.values())[0]
        dy = list(self.offset.values())[1]
        return {'x': point['x'] + dx, 'y': point['y'] + dy}


parsers = lambda point, x: ast.literal_eval(point) if x == True else point
# returns a dictionary, "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}

def conditionalParse(point):
    parser = parsers(point, (str(type(point)) == "<class 'str'>"))
    return parser


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    "{'x': 20,'y': 20}",
    {'x': 30, 'y': 30},
]
print('polyline :', '\n', polyline)
shift = Shift({'dx': 10, 'dy': -5})  # create an object
polyline = list(map(conditionalParse, polyline))
path = list(map(shift.move, polyline))
print('path :', '\n', path)
