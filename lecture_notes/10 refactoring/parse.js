'use strict';

const shift = ({ a, b }) => ({ x, y }) => ({ x: x + a, y: y + b });

const check_type = (line) =>
  (typeof line !== 'object' ? JSON.parse(line) : line);

const offset = shift({ a: 10, b: -5 });

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const checked_type = polyline.map(check_type);
const path = checked_type.map(offset);
console.log({ path });