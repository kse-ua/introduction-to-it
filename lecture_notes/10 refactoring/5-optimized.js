'use strict';

const move = ({ dx, dy }) => ({ x, y }) => ({ x: x + dx, y: y + dy });

const conditionalParse = (item) =>
  typeof item === 'string' ? JSON.parse(item) : item;

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const offset = move({ dx: 10, dy: -5 });
const parsed = polyline.map(conditionalParse);
const path = parsed.map(offset);
console.log({ path });
