""""
'use strict';

const shift = (offset, points) => {
  const moved = points.map((point) => {
    const type = typeof point;
    if (type === 'object') {
      point.x += offset.x;
      point.y += offset.y;
    } else {
      point = JSON.parse(point);
      point.x += offset.x;
      point.y += offset.y;
    }
    return point;
  });
  return moved;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const path = shift({ x: 10, y: -5 }, polyline);
console.log({ path });
"""

# ---------------------------------------------------------------------------------------------------
import ast  # abstract syntax tree, conversion to code "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}

def shift(offset, points):

    def _shift(point):
        _type = str(type(point))  # type definition, translation to string
        if _type == "<class 'dict'>":  # python dict = javascript object
            point['x'] += offset['x']
            point['y'] += offset['y']
        else:
            point = ast.literal_eval(point)  # returns a dictionary, "{'x': 20,'y': 20}" >> {'x': 20,'y': 20}
            point['x'] += offset['x']
            point['y'] += offset['y']
        return point

    moved = list(map(_shift, points))

    return moved


polyline = [
    {'x': 0, 'y': 0},
    {'x': 10, 'y': 10},
    "{'x': 20,'y': 20}",
    {'x': 30, 'y': 30},
]


print('polyline :', '\n', polyline)
"""  initial data output
polyline :
{'x': 0, 'y': 0}
{'x': 10, 'y': 10}
"{'x': 20,'y': 20}"
{'x': 30, 'y': 30}
"""

path = shift({'x': 10, 'y': -5}, polyline)

print('path :', '\n', path)
"""  result output
path :
{'x': 10, 'y': -5}
{'x': 20, 'y': 5}
{'x': 30, 'y': 15}
{'x': 40, 'y': 25}
"""

