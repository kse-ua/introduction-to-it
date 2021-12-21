'use strict';

const elementType = (point) =>
  (typeof point === 'object' ? point : JSON.parse(point) ); //a ternary operator here
  
const shift = ({ coordinate1, coordinate2 }) => ({ x, y }) => ({ x: x + coordinate1, y: y + coordinate2 });

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const type = polyline.map(elementType);
const newShift = type.map( shift({ coordinate1: 10, coordinate2: -5 }) );
console.log({ newShift });
