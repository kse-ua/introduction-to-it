'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

// del last elem from the array
ages.pop();

// add elem at the end of the array
ages.push(21);

// del first elem from the list
ages.shift();

// add elem at the beggining of the list
ages.unshift(9);

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });
