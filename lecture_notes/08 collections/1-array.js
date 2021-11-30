'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

// removing/adding to the back
ages.push(25);
ages.pop();
// removing/adding to the front
ages.unshift(25);
ages.shift();
// reverse method 
ages.reverse();
console.log(ages)
