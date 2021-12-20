"use strict";

const parse = (point) => {
    return typeof point === "object" ? point : JSON.parse(point);
};

const shift = (offset, points) => {
    let modifiedPoints = [];
    points.forEach((point) => {
        point = parse(point);
        point.x += offset.x;
        point.y += offset.y;
        modifiedPoints.push(point);
    });
    return modifiedPoints;
};

const polyline = [
    { x: 0, y: 0 },
    { x: 10, y: 10 },
    '{ "x": 20, "y": 20 }',
    { x: 30, y: 30 },
];

const result = shift({ x: 10, y: -5 }, polyline);
console.log({ result });
