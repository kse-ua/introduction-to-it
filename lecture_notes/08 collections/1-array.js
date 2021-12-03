'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });

ages.push(21);
// add element to the end
console.log(ages);

ages.pop();
// remove the last element
console.log(ages);

ages.unshift(1);
// add element to the beginning
console.log(ages)
;
ages.shift(1);
// remove element from the beginning
console.log(ages)
;
