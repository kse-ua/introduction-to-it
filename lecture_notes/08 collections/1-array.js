'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

const addAtEnd = ages.push(21)
console.log(addAtEnd);
const deleteFromEnd = ages.pop()
console.log(deleteFromEnd);
const addAtTop = ages.unshift(9)
console.log(addAtTop);
const deleteFromTop = ages.shift()
console.log(deleteFromTop);

console.log({ first, last });
