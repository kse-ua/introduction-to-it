'use strict';

const shift = (offset) => (point) => {   /* here "point" 
stands for a line of an array 
"polyline" (why? see line 24 when "shift" function is called) */
  const type = typeof point;
  if (type === 'object') {
    point.x += offset.coordinate1;
    point.y += offset.coordinate2;
  } else {
    point = JSON.parse(point);
    point.x += offset.coordinate1;
    point.y += offset.coordinate2;
  }
  return point;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const newShift = polyline.map(shift({ coordinate1: 10, coordinate2: -5 })); 
/* the function "shift" is executed for EVERY line of "polyline"
because the "map" method is used */
console.log({ newShift });
