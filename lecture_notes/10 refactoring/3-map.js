'use strict';

function shift(offset, points) {
    points.forEach(function (point) {
        point.x += offset.x;
        point.y += offset.y;
    });
    return points;
}

function parser(point){
    if (typeof point === 'string')
        return JSON.parse(point);
    return point;
}

let polyline = [
    {x: 0, y: 0},
    {x: 10, y: 10},
    '{"x": 20, "y": 20}',
    {x: 30, y: 30}
]

polyline = polyline.map(function(e) {
    e = parser(e);
    return e;
});

shift({x: 10, y: -5}, polyline);
console.log(polyline);
