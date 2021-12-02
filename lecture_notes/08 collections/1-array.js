'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });

ages.push(21); // # Add at the end of array
console.log(ages);
ages.pop(); // remove at the end of array
console.log(ages);
ages.shift(); // Add at the top of array
console.log(ages);
ages.unshift(11); // remove at the top of array
console.log(ages);
