'use strict';

// Implementation

// in python use def
const getFirstAndLast = (array) => {
  // the same
  const first = array[0];
  // in python use [number]
  const last = array[array.length - 1];
  // the same
  return { first, last };
};

// Usage
// the same
const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
// the same
const { first, last } = getFirstAndLast(ages);
// print function in python
console.log({ first, last });
