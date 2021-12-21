"use strict";

const parse = (point) => {
    return typeof point === "object" ? point : JSON.parse(point);
};

const move = (offset) => (point) =>{
    point.x += offset.x;
    point.y += offset.y;
    return point
};

const polyline = [
    { x: 0, y: 0 },
    { x: 10, y: 10 },
    '{ "x": 20, "y": 20 }',
    { x: 30, y: 30 },
];


const offset = move({ x: 10, y: -5 });
const path = polyline.map(parse).map(offset);
console.log({ path });
