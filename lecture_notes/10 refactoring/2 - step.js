"use strict";
//Here we create function in function using multi arrows
const move = (offset) => (point) => {
  point.x += offset.x;
  point.y += offset.y;
  return point;
};

const conditionalParse = (item) => {
  //Checking for 'object' using Parsing
  if (typeof item === "object") return item;
  return JSON.parse(item);
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const offset = move({ x: 39, y: -100 });
const parsed = polyline.map(conditionalParse);
//Now 'map' is outside function
const path = parsed.map(offset);
console.log({ path });

