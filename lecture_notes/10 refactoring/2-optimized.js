'use strict';

const moove = (point) => {
  point.x += offset.x;
  point.y += offset.y;
  return point;
};

const parse = (point) => {
  if (typeof point === 'object') {
    return point 
  };
  return JSON.parse(point);
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const shift = (points) => {
  const parsed = points.map(parse);
  const mooved = parsed.map(moove);
  return mooved;
};

const offset = { x: 10, y: -5 };
console.log(shift(polyline));
