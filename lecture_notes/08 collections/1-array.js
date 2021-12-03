'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const newElement1 = 5, newElement2 = 10;
ages.pop();
ages.push(newElement1, newElement2);
ages.shift();
ages.unshift(newElement1);

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });
