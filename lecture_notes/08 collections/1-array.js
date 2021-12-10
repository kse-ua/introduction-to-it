'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

console.log({'first': first, 'last': last});

ages.push(21);
console.log(ages);

ages.pop();
console.log(ages);

ages.shift();
console.log(ages);

ages.unshift(12);
console.log(ages);
