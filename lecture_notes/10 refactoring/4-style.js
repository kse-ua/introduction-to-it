'use strict';

let parse_point = (point) => {
    return (typeof point === 'object' ? point: JSON.parse(point))
}

let shift = (offset) => (point) => {
    point.x += offset.x;
    point.y += offset.y;
    return point;
};

const polyline = [
    { x: 0, y: 0 },
    { x: 10, y: 10 },
    '{ "x": 20, "y": 20 }',
    { x: 30, y: 30 },
];

const to_offset = {x: 10, y: -5}
const parsed = polyline.map(parse_point)
const result = parsed.map(shift(to_offset))
console.log({ result })