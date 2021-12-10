'use strict';

// Implementation
const concat = (arr1, arr2) => arr1.concat(arr2);

const altConcat = (arr1, arr2) => {
    const arr = [];
    arr.push(...arr1);
    arr.push(...arr2);
    return arr;
    };

// Usage
const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];
const ages = concat(schoolAges, studentAges);

console.log({ ages });

const altAges = altConcat(schoolAges, studentAges);
console.log({ altAges });
