'use strict';

const move = (offset) => (point) => {
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
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const offset = move({ x: 10, y: -5 });
const path = polyline.map(offset);
console.log({ path });

