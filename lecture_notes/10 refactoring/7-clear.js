'use strict';

const shift = (offset) => (dot) => {
  const moved = {
    x: dot.x += offset.dx,
    y: dot.y += offset.dy,
  };
return moved;
};

const parsers = { string: JSON.parse, object: (obj) => obj };

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

const doTask = () => {
  const move = shift({ dx: 10, dy: -5 });
  const parsed = polyline.map(conditionalParse);
  const path = parsed.map(move);
  console.log({ path });
};

return doTask.call();
