"use strict";

const move = (offset) => (point) => {
    const moving = {
        x: point.x + offset.dx,
        y: point.y + offset.dy,
    };
    return moving;
};

const conditionalParse = (item) =>
    (typeof item === 'string' ? JSON.parse(item) : item);

const coordinates = [
    {x: 0, y: 0},
    {x: 10, y: 10},
    '{ "x": 20, "y": 20 }',
    {x: 30, y: 30},
];

const offset = move({ dx: 40, dy: -50 });
const parsed = coordinates.map(conditionalParse);
const path = parsed.map(offset);
console.log({path});

