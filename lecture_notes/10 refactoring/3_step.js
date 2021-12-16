'use strict';

const shift = (offset, point) => {
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
        return points;
}

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];


const startPoint = { x: 10, y: -5 };
const result = polyline.map(shift(startPoint));
console.log({ result });
