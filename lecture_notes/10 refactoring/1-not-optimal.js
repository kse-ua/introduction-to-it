"use strict";
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Enter coordinate X: ', (x) => {
  rl.question('Enter coordinate Y: ', (y) => {
    const x = Number(X);
    const y = Number(Y);

    const move = (coords) => (point) => {
      point.x += coords.x;
      point.y += coords.y;
      return point;
    };

    const conditionalParse = (item) => {
      if (typeof item === "object") return item;
      return JSON.parse(item);
    };

    const coordinates = [
      { x: 0, y: 0 },
      { x: 10, y: 10 },
      '{ "x": 20, "y": 20 }',
      { x: 30, y: 30 },
    ];

    const parsed = coordinates.map(conditionalParse);
    const coords = move({ x: x, y: y });
    const path = parsed.map(coords);
    console.log({ path });

    rl.close();
  });
});
