'use strict';

const schoolаges = [10, 12, 15, 15];
const studentаges = [17, 18, 18, 19, 20];
const ages = (schoolAges.concat(studentAges));
const getFirstAndLast = (array) => ({
  first: array[0],
  last: array[array.length - 1],
});
const result = getFirstAndLast(ages);
console.log(result);
