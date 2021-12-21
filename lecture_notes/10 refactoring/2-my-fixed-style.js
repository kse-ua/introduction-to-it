'use strict';

const addTwoObj = (addend, points) => {
  points.forEach((point) => {
    const type = typeof point;
    if (type === 'object') {
      point.x += addend.x;
      point.y += addend.y;
    } else {
      let i = points.indexOf(point);
      points[i] = JSON.parse(point);
      points[i].x += addend.x;
      points[i].y += addend.y;
    }
  });
  return points;
};

const arrOfObj = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

addTwoObj({ x: 10, y: -5 }, arrOfObj);
console.log({ polyline });
