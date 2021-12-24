"use strict";

const shift = (offset, points) => {
  for (const point of points) {
    const type = typeof point;
    if (type === "object") {
      point.x += offset.x;
      point.y += offset.y;
    } else {
      const i = points.indexOf(point);
      points[i] = JSON.parse(point);
      points[i].x += offset.x;
      points[i].y += offset.y;
    }
  }

  return points;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

shift({ x: 10, y: -5 }, polyline);
console.log({ polyline });
