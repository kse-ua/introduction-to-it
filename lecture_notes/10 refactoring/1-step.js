'use strict';

// Function that iterates each element in polyline checks if it's an obj; parse it using JSON.
const point_parse = (points) => {
    return points.map((point) => {
        if (typeof point != 'object') {
            return JSON.parse(point);
        } else {
            return point
        }
    });
}

// Taking a result from PointParse and shifting it
const points_shift = (arr, dot_param) => {
    return arr.map((dot) => {
        dot['x'] += dot_param['x']
        dot['y'] += dot_param['y']
        return dot;
    });
}

const polyline = [
    { x: 0, y: 0 },
    { x: 10, y: 10 },
    '{ "x": 20, "y": 20 }',
    { x: 30, y: 30 },
];


const path = point_parse(polyline)
console.log(points_shift(path, { x: 10, y: -5 }))
