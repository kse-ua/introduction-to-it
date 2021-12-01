'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });

ages.pop();
ages.push(25);
ages.shift();
ages.unshift(8);

console.log(ages);

delete ages[3];
ages[3] = 16;
console.log(ages);
const teens = ages.slice(1, 5);
console.log(teens);
