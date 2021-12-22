'use strict';

const actionsType = {
  string: (element) => JSON.parse(element),
  object: (element) => element,
};

/* called this new function (which is actually a dictionary) "actionsType"
cuz it describes actions that need to be done
with the element depending on its type.
This dictionary stores element's type as 'key',
and actions on this element(function) as its 'value' */

const elementType = (point) => actionsType[typeof point](point);
/* "actionsType[typeof point](point)"  is a function
 which firstly takes point's type ("actionsType[typeof point]")
 and then returns a function depending on
 the type of this point, taking point as an argument */

const shift = ({ coordinate1, coordinate2 }) => ({ x, y }) => ({
  x: x + coordinate1,
  y: y + coordinate2,
});

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const type = polyline.map(elementType);
const newShift = type.map(shift({ coordinate1: 10, coordinate2: -5 }));
console.log({ newShift });
