'use strict';

class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  static get parsers() {
    return {
      object: (obj) => obj,
      string: JSON.parse,
    };
  }

  static parse(object) {
    const parser = Point.parsers[typeof object];
    const parsedPoint = parser(object);

    return new Point(parsedPoint.x, parsedPoint.y);
  }

  move(offset) {
    const x = this.x + offset.dx;
    const y = this.y + offset.dy;

    return new Point(x, y);
  }
}

const offset = { dx: 10, dy: -5 };
const rawData = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];
const polyline = rawData.map(Point.parse);
const path = polyline.map((point) => point.move(offset));
console.log({ path });
