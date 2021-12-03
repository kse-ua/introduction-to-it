'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
ages.splice(4, 1);
const first = ages[0];
const last = ages[2];
ages.splice(4, 1);
ages.splice(5, 1, 100);
ages.push(201);
ages.shift();
ages.unshift(0);
console.log({ first, last });
console.log(ages);
