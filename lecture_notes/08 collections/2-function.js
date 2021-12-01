
// Implementation

//To declare function in python we use def
const getFirstAndLast = (array) => {
    // This line is the same in python
    const first = array[0]; 
    // Here we use length to find the last element, in python we use [number]
    const last = array[array.length - 1]; 
    // This line is the same in python
    return { first, last }; 
};

// Usage

// This line is the same in python
const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]; 
// This line is the same in python
const { first, last } = getFirstAndLast(ages); 
// We use print function in python in comparison to console.log in Js
console.log({ first, last });  
