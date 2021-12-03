'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
console.log("Original list:", ages);

 // different functions for REMOVING LAST element:
 
 function usingPop(ages) {
     const copyAges = ages.slice();
     copyAges.pop();
     return copyAges;
 }
 
function usingLength(ages) {
    const copyAges = ages.slice();
    copyAges.length = 8;
    return copyAges;
}
 
function usingSplice(ages) {
    const copyAges = ages.slice();
    copyAges.splice(8, 1);
    return copyAges;
}

 // some functions for ADDING LAST element:
 
 function usingPush(ages) {
     const copyAges = ages.slice();
     copyAges.push(23); 
     return copyAges;
 }

function usingConcat(ages) {
    const copyAges = ages.slice();
    const newList = [235];
    const updatedcopyAges = ages.concat(newList);
    return updatedcopyAges;
}

function usingIndex(ages) {
    const copyAges = ages.slice();
    copyAges[9] = 55;
    return copyAges;
}

 // various functions for DELETING FIRST element:
 
function usingShift(ages) {
    const copyAges = ages.slice();
    copyAges.shift();
    return copyAges;
}

function usingSplice(ages) {
    const copyAges = ages.slice();
    copyAges.splice(0, 1);
    return copyAges;
}

 // a function for ADDING FIRST element:
 
 function usingUnshift(ages) {
     const copyAges = ages.slice();
     copyAges.unshift(7);
     return copyAges;
 }

console.log("Removing last element using the:")
console.log("- 'pop' function:", usingPop(ages))
console.log("- length limitation method:", usingLength(ages))
console.log("- 'splice' technique:", usingSplice(ages))
console.log("Adding last element using the:")
console.log("~ 'push' function:", usingPush(ages))
console.log("~ 'concat' method:", usingConcat(ages))
console.log("~ index of a new element", usingIndex(ages))
console.log("Deleting first element using the:")
console.log("-- 'shift' function:", usingShift(ages))
console.log("-- 'splice' method:", usingSplice(ages))
console.log("Adding a new first element to the list:")
console.log("- using 'unshift' function:", usingUnshift(ages))
