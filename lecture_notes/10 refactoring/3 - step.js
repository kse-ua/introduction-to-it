'use strict';

const move =
  ({ dx, dy }) =>
    ({ x, y }) => ({
    //Returning result
      x: x + dx,
      y: y + dy,
    });

const coordParse = (item) =>
  (typeof item === 'string' ? JSON.parse(item) : item);

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const offset = move({ dx: 45, dy: 54 });
const parsed = polyline.map(coordParse);
const path = parsed.map(offset);
console.log({ path });
