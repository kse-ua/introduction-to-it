'use strict';

function shift(offset, points) {
    points.forEach(function (point) {
        point.x += offset.x
        point.y += offset.y
    });
    return points;
}

function parser(points) {
    points.forEach(
        function (point) {
            if (typeof (point) === "string") {
                var i = points.indexOf(point)
                points[i] = JSON.parse(points[i])
            }
        });
    return points;
}

let polyline = [
    {x: 0, y: 0},
    {x: 10, y: 10},
    '{"x": 20, "y": 20}',
    {x: 30, y: 30}
]

polyline = parser(polyline)
shift({x: 10, y: -5}, polyline)
console.log(polyline)
