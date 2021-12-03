'use strict';

// Implementation

const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];
const ages = schoolAges.concat(studentAges);

// Usage

const first = schoolAges[0]
const last = studentAges[studentAges.length - 1]

console.log({ first, last });
console.log("All ages are:", ages);
