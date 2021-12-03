'use strict';

// Implementation

// Use lambda instead
const getFirstAndLast = (array) => ({
  first: array[0], // The same
  // In python use [number of last]
  last: array[array.length - 1],
});

// Usage

// The same
const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
// The same
const { first, last } = getFirstAndLast(ages);
// In python 'console.log'
console.log({ first, last });
