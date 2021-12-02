'use strict';

// Implementation

const getFirstAndLast = (array) => ({
  first: array[0],
  last: array[array.length - 1],
});

const concat = (arr1, arr2) => {
  const arr = arr1.slice();
  arr.push(...arr2);
  return arr;
};

// Usage

const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];
const ages = concat(schoolAges, studentAges);
console.log({ ages });
const { first, last } = getFirstAndLast(ages);
console.log({ first, last });
