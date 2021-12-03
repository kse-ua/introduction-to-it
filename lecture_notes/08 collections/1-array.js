'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

let newElement1, newElement2 = 5, 10;
ages.pop();
ages.push(newElement1, newElement2);
ages.unshift();
ages.shift();

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });
