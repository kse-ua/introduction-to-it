'use strict';

const shift = (offset) => (point) => {
  point.x += offset.x;
  point.y += offset.y;
  return point;
};

const typeCheck = (line) => {
  if (typeof line !== 'object') return JSON.parse(line);
  return line;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const offset = shift({ x: 10, y: -5 });
const checked = polyline.map(typeCheck);
const path = checked.map(offset);
console.log({ path });
