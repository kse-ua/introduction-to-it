'use strict';

// Implementation

//In python we don't declare a function, we use lambda instead
const getFirstAndLast = (array) => ({ 
  first: array[0], //This line is the same in python
  // Here we use length to find the last element, in python we [number of last]
  last: array[array.length - 1], /
});

// Usage

// This line is the same in python
const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]; 
// This line is the same in python
const { first, last } = getFirstAndLast(ages); 
// We use print function in python in comparison to 'console.log'
console.log({ first, last }); 
