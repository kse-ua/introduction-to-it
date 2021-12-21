""""
'use strict';

const move = (offset) => (point) => {
  const moved = {
    x: point.x + offset.dx,
    y: point.y + offset.dy,
  };
  return moved;
};

const parsers = {
  string: JSON.parse,
  object: (obj) => obj,
};

const conditionalParse = (item) => {
  const parser = parsers[typeof item];
  return parser(item);
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const offset = move({ dx: 10, dy: -5 });
const parsed = polyline.map(conditionalParse);
const path = parsed.map(offset);
console.log({ path });
"""

# ------------------------------------------------------------------------------------------------
import ast  # abstract syntax tree, conversion of code "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}


class PointXY:
    def __init__(self, point):  # python __init__ = javascript constructor
        x = list(point.values())[0]  # ['x'] ['dx']
        y = list(point.values())[1]  # ['y'] ['dy']
        self.point = point
        self.x, self.y = x, y  # x: point['x'] >> self.x >> point.x , y: ...
        self.dx, self.dy = x, y  # x: offset['dx'] >> offset.dx >> offset.dx , y: ...

def move(point):
    moved = {'x': point.x + offset.dx, 'y': point.x + offset.dy}
    return moved

def parsers(point, x):
    # returns a dictionary, "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}
    _point = ast.literal_eval(point) if x else point  # ternary operator
    return PointXY(_point)  # create an object

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
offset = PointXY({'dx': 10, 'dy': -5})  # create an object
polyline = list(map(conditionalParse, polyline))
path = list(map(move, polyline))
print('path :', '\n', path)

