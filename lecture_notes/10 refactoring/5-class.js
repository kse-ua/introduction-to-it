'use strict';

class Shift{
    constructor(x, y) {
        this.x = x
        this.y = y
    }

    add(point){
        point.x += this.x
        point.y += this.y
        return point
    }
}

let parse_point = (point) => {
    return (typeof point === 'object' ? point: JSON.parse(point))
}

const polyline = [
    { x: 0, y: 0 },
    { x: 10, y: 10 },
    '{ "x": 20, "y": 20 }',
    { x: 30, y: 30 },
];

const shift = new Shift(10, -5)
const parsed = polyline.map(parse_point)
const result = parsed.map((point) => shift.add(point))
console.log({ result })