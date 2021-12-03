'use strict';

// Implementation

//use lambda instead
const getFirstAndLast = (array) => ({

  first: array[0],   // the same
  // in python use [number of last]
  last: array[array.length - 1],
});

// Usage
// the same
const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
// the same
const { first, last } = getFirstAndLast(ages);
// in python 'console.log'
console.log({ first, last });
