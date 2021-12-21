""""
'use strict';

class Shift {
  constructor(offset) {
    this.offset = offset;
  }

  move(point) {
    return {
      x: point.x + this.offset.dx,
      y: point.y + this.offset.dy,
    };
  }
}

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

const shift = new Shift({ dx: 10, dy: -5 });
const parsed = polyline.map(conditionalParse);
const path = parsed.map((point) => shift.move(point));
console.log({ path });
"""

# ------------------------------------------------------------------------------------------------
import ast  # abstract syntax tree, conversion to code "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}


class Shift:
    def __init__(self, point):  # python __init__ = javascript constructor
        self.point = point  # python self = javascript this
        self.x = list(point.values())[0]  # point['x'] >> self.x
        self.y = list(point.values())[1]  # point['y'] >> self.y
        self.dx = self.x
        self.dy = self.y

    def move(self, point):
        return {'x': point.x + self.dx, 'y': point.y + self.dy}  # self >> offset, self.x >> offset.dx ...


def parsers(point, x):
    # returns a dictionary, "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}
    _point = ast.literal_eval(point) if x else point  # ternary operator
    return Shift(_point)   # create an object

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

