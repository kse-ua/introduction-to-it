'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
console.log('Here\'s the initial version of our array:', ages);
const first = ages[0];
const last = ages[ages.length - 1];
console.log('Let\'s see the original beginning and end', { first, last }, '\n');

ages.pop();
ages.push(21);
console.log('Now we change the end of our array:', ages);

ages.shift();
ages.unshift(5);
console.log('And now we change the start of our array:', ages);

const newFirst = ages[0];
const newLast = ages[ages.length - 1];

console.log('\nAnd so let\'s see the new values:', { newFirst, newLast });
