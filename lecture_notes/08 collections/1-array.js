'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });

// Remove elements from the end
ages.pop();

// Remove elements from the beginning
ages.shift();

// Add elements to the beginning
ages.unshift(4, 13);

// Add elements to the end
ages.push(25, 31)

console.log("The new list is:", ages)
