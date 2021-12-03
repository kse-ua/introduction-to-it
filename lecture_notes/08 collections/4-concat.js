'use strict';

const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];

const newArray = schoolAges.concat(studentAges);
const first = newArray[0];
const last = newArray[newArray.length - 1];

console.log({ first, last });
