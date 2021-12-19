'use strict';

const shift = (offset) => (point) => {   /* here "point" stands for a line of
  an array "polyline" (why? see line 24 when "shift" function is called) */
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

const newShift = polyline.map( shift({ x: 10, y: -5 }) ); /* the function
  "shift" is executed for EVERY line of "polyline" because the "map() method" is used */
console.log({ newShift });
