'use strict';

const shift = (offset) => (dot) => {
  const type = typeof dot;
  if (type === 'object') {
    dot.x += offset.x;
    dot.y += offset.y;
  } else {
    dot = JSON.parse(dot);
    dot.x += offset.x;
    dot.y += offset.y;
  }
  return dot;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const path = polyline.map(shift({ x: 10, y: -5 }));
console.log({ path });
