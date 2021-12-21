'use strict';

// declaring a separate function for checking a type of "point"
const elementType = (point) => {
  if (typeof point === 'object') 
     return point;
  else 
     return JSON.parse(point);
};

const shift = (offset) => (point) => {
  point.x += offset.coordinate1;
  point.y += offset.coordinate2;
  return point;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const type = polyline.map(elementType); /* the function "elementType" is
    executed for EVERY line of "polyline" because the "map() method" is used */
const newShift = type.map( shift({ coordinate1: 10, coordinate2: -5 }) );
console.log({ newShift });
