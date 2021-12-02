'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });

ages.push(-1003);
console.log(ages[ages.length - 1]);

ages.pop();
console.log(ages[ages.length - 1]);

ages.unshift(-832);
console.log(ages[0]);

ages.shift();
console.log(ages[0]);

ages.sort();
console.log(ages);
