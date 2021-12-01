'use strict';

const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];
const NewSet = schoolAges.concat(studentAges);
const first = NewSet[0];
const last = NewSet[NewSet.length - 1];


console.log({ first, last });
