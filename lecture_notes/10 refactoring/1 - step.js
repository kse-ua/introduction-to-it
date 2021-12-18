'use strict';

const shift = (offset, points) => {
  //Here we create new set using map
  const moving = points.map((point) => {
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
  });
  return moving;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const path = shift({ x: 50, y: -40 }, polyline);

console.log({ path });
