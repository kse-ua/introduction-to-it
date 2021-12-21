'use strict';

class Shift {
  constructor(offset) {
    this.offset = offset;
  }

  move(point) {
    // removed the code
    /*
    return {
      x: point.x + this.offset.dx,
      y: point.y + this.offset.dy,
    };
    */

    // added code
    const { dx, dy } = this.offset;
    return {x: point.x + dx,y: point.y + dy};
  }
}

const parsers = {
  string: JSON.parse,
  object: (obj) => obj,
};

const conditionalParse = (item) => {
  const parser = parsers[typeof item];
  return parser(item);
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const shift = new Shift({ dx: 10, dy: -5 });
const parsed = polyline.map(conditionalParse);
const path = parsed.map((point) => shift.move(point));
console.log({ path });
