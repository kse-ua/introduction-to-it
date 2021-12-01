'use strict';

// Implementation

const getFirstAndLast = (array) => ({ //In python we don't declare a function, we use lambda instead
    first: array[0], //This line is the same in python
    last: array[array.length - 1], // Here we use length to find the last element, in python we [number of last]
});

// Usage

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]; // This line is the same in python
const { first, last } = getFirstAndLast(ages); // This line is the same in python
console.log({ first, last }); // We use print function in python in comparison to 'console.log' in Js
