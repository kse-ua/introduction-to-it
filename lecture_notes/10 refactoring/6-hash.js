'use strict';

const shift =
  ({ a, b }) =>
    ({ x, y }) => ({ x: x + a, y: y + b });

const typeCheck = { string: JSON.parse, object: (x) => x };

const genCheck = (line) => typeCheck[typeof line](line);

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const offset = shift({ a: 10, b: -5 });
const checked = polyline.map(genCheck);
const path = checked.map(offset);
console.log({ path });
