'use strict';

const parsePoint = (point) => {
  if (typeof point === 'object') point;
  return JSON.parse(point);
};

const shift = (offset) => (point) => {
  point.x += offset.x;
  point.y += offset.y;
  return point;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const toOffset = { x: 10, y: -5 };
const parsed = polyline.map(parsePoint);
const result = parsed.map(shift(toOffset));
console.log({ result });
