'use strict';

const shift = (offset, points) => {
  const moved = points.map((point) => {
    if (typeof point !== 'object') {
      point = JSON.parse(point);
    }
    point.x += offset.x;
    point.y += offset.y;

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

const offset = { x: 10, y: -5 };
console.log(shift(offset, polyline));
