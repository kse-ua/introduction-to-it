'use strict';
const moove = (point, offset) => {
  point.x += offset.x;
  point.y += offset.y;
  return point;
};

const parse = (cord) => (typeof cord === 'object') ? cord : JSON.parse(cord);

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 }
];
const offset = { x: 10, y: -5 };

const parsed = polyline.map(parse);
const mooved = parsed.map(parsed => moove(parsed, offset));
console.log(mooved);

