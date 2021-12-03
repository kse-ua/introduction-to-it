'use strict';

const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];
const NewArray = schoolAges.concat(studentAges);
const first = NewArray[0];
const last = NewArray[NewArray.length - 1];


console.log({ first, last });
