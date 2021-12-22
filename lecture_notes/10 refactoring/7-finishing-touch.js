'use strict';

const actionsType = {
    string: (element) => JSON.parse(element),
    object: (element) => element,
};  

const elementType = (point) => actionsType[typeof point](point); 

class BigMovement {
    constructor(coordinate1, coordinate2) {
        this.coordinate1 = coordinate1;
        this.coordinate2 = coordinate2;
    }
    
    shift(point) {
    point.x += this.coordinate1;
    point.y += this.coordinate2;
    return point;
  }
}

const polyline = [
  { x: 0, y: 0 },
  { x: 10, y: 10 },
  '{ "x": 20, "y": 20 }',
  { x: 30, y: 30 },
];

const move = new BigMovement(10, -5);
const type = polyline.map(elementType);
const newShift = type.map( (point) => move.shift(point) );
console.log({ newShift });
