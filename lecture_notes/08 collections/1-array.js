 'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

let newLen = ages.push(21) //Add an item to the end of an Array
console.log(ages)
let prevLen = ages.pop() //Remove an item from the end of an Array
console.log(ages)

newLen = ages.unshift(9) //Add an item to the beginning of an Array
console.log(ages)
prevLen = ages.shift() //Remove an item from the beginning of an Array
console.log(ages)

console.log({ first, last });
