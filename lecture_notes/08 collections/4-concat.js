'use strict';

// Implementation

const get_first_and_last = (array) => ({
  first: array[0],
  last: array[array.length - 1],
});

const concat = (arr1, arr2) => arr1.concat(arr2);

// Usage

const school_ages = [10, 12, 15, 15];

const student_ages = [17, 18, 18, 19, 20];

const ages = school_ages.concat (student_ages);

const { first, last } = get_first_and_last(ages);
console.log({'first': first, 'last': last});
