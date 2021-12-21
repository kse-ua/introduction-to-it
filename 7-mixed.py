""""
'use strict';

class Shift {
  constructor(offset) {
    this.offset = offset;
  }

  move({ x, y }) {
    const { dx, dy } = this.offset;
    return { x: x + dx, y: y + dy };
  }
}

const parsers = {
  string: JSON.parse,
  object: (x) => x,
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

