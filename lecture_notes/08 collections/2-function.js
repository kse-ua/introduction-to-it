'use strict';

// Implementation

const get_first_and_last = (array) => {
  const first = array[0];
  const last = array[array.length- 1];
  return { first, last };
};

// Usage

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
const { first, last } = get_first_and_last(ages);
console.log({ first, last });

