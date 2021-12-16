'use strict';

const shift = (offset) => (point) => {
  point.x += offset.x;
  point.y += offset.y;
  return point;
};

const conditional = (item) => {
  if (typeof item === 'object') return item;
  return JSON.parse(item);
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const offset = shift({ x: 10, y: -5 });
const parsed = polyline.map(conditional);
const shifted = parsed.map(offset);
console.log({ shifted });
