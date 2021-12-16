'use strict';

const shift = (points) => {
  const moved = points.map((point) => (offset) => {
    const type = typeof point;
    if (type === 'object') {
      point.x += offset.x;
      point.y += offset.y;
    } else {
      const i = points.indexOf(point);
      point = JSON.parse(point);
      point.x += offset.x;
      point.y += offset.y;
    }
    return point
  });
  return moved;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];


const result = shift({ x: 10, y: -5 }, polyline);
console.log({ result });
