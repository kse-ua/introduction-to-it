'use strict';

const shift = (offset, points) => {
  const shifted = points.map((dot) => {
    const type = typeof dot;
    if (type === 'object') {
      dot.x += offset.x;
      dot.y += offset.y;
    } else {
      dot = JSON.parse(dot);
      dot.x += offset.x;
      dot.y += offset.y;
    }
    return dot;
  });
  return shifted;
};

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const path = shift({ x: 10, y: -5 }, polyline);
console.log({ path });
