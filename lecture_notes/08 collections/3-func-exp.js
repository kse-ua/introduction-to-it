'use strict';

// Implementation

const get_first_and_last = (array) => ({
  first: array[0],
  last: array[array.length - 1],
});

// Usage

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
const { first, last } = get_first_and_last(ages);
console.log({ 'first': first, 'last': last});


