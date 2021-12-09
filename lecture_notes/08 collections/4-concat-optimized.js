'use strict';

// Implementation
const concat = (arr1, arr2) => arr1.concat(arr2)

const altConcat = (arr1, arr2) => {
const arr = [];
// arr.push(arr1);
// arr.push(arr2);
for (const value of arr1) {
    arr.push(value) 
}
for (const value of arr2) {
    arr.push(value)
}
return arr;
}

// Usage
const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];
const ages = concat(schoolAges, studentAges);

console.log({ ages });

const arr = altConcat(schoolAges, studentAges);
console.log({ arr })