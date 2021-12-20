'use strict';

// Function that iterates each element in polyline checks if it's an obj; parse it using JSON.
const point_parse = (points) => {
    return typeof points != 'object' ? JSON.parse(points) : points
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

// Iterate polyline's elements for PointParse and then put it as a parameter
const LineIter = polyline.map(point_parse)
console.log(points_shift(LineIter, { x: 10, y: -5 }))
