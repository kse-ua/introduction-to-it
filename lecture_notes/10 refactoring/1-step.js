'use strict';

const pointParse = (points) => {
  points.map((point) => {
    if (typeof point !== 'object') {
      return JSON.parse(point);
    } else {
      return point;
    }
  });
  return points;
};

// Taking a result from PointParse and shifting it
const pointsShift = (arr, dotParam) => {
  arr.map((dot) => {
    dot['x'] += dotParam['x'];
    dot['y'] += dotParam['y'];
    return dot;
  });
  return arr;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const path = pointParse(polyline);
console.log(pointsShift(path, { x: 10, y: -5 }));
