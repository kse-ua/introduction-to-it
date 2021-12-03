'use strict';

// Implementation

const concat = (arr1, arr2) => {
  const arr = arr1.slice();
  arr.push(...arr2);
  return [arr[0], arr[arr.length - 1]];
};

// Usage

const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];
const firstAndLast = concat(schoolAges, studentAges);
console.log( firstAndLast );
