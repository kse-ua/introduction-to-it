"use strict";

const parsePoint = (point) => {
  if (typeof point === 'object') {
    return point;
  } else {
    return JSON.parse(point);
  }
};

const shift = (offset, points) => {
  points.forEach((point) => {
    point.x += offset.x;
    point.y += offset.y;
  });
  return points;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ x: 20, y: 20 }',
  { x: 30, y: 30 },
];

const toOffset = { x: 10, y: -5 };
const parsed = polyline.map(parsePoint);
shift(toOffset, parsed);
console.log({ parsed });
