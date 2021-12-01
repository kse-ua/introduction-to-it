'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

// Del last elem
ages.pop();

ages.push(21, 22)

// Add elements at the beginning of a list
ages.unshift(8,9)

// Del the first elem from a list
ages.shift()


const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });
