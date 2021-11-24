'use strict';

// Implementation

const getFirstAndLast = (array) => ({
  first: array[0],
  last: array[array.length - 1],
});

const concat = (arr1, arr2) => [...arr1, ...arr2];

// Usage

const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];
const ages = concat(schoolAges, studentAges);
const { first, last } = getFirstAndLast(ages);
console.log({ first, last });
