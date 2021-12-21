'use strict';

const addTwoObj = addend => point => {x: point.x + addend.x; y: point.y + addend.y;}

const detectType = item => (typeof item === 'string' ? JSON.parse(item) : item);

const arrOfObj = [
    { x: 0, y: 0 },
    { x: 10, y: 10 },
    '{ "x": 20, "y": 20 }',
    { x: 30, y: 30 },
];

const offset = addTwoObj({ x: 10, y: -5 });
const parsed = arrOfObj.map(detectType);
const res = parsed.map(offset);
console.log({ res });
