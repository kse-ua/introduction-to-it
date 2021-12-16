'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

ages.shift();
ages.unshift(5);

ages.pop();
ages.push(5);

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });
