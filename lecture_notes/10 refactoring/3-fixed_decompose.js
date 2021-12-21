'use strict';

const addTwoObj = (addend, point) => {
    point.x += addend.x;
    point.y += addend.y;
    return point;
}

const addingArrAndObj = (addend, points) => {
    points.forEach((point) => {
        const type = typeof point;
        if (type === 'object') {
            point = addTwoObj(addend, point);
        } else {
            point = JSON.parse(point);
            point = addTwoObj(addend, point);
        }
    });
    return points;
};

const arrOfObj = [
    { x: 0, y: 0 },
    { x: 10, y: 10 },
    '{ "x": 20, "y": 20 }',
    { x: 30, y: 30 },
];

addingArrAndObj({ x: 10, y: -5 }, arrOfObj);
console.log({ arrOfObj });
