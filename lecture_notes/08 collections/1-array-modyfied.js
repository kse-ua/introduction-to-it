'use strict';

//usage:
const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
const first = ages[0];
const last = ages[ages.length - 1];
const arrayForNewElements = ages.reverse();
const newFilterdArray = arrayForNewElements.filter((element) => element > 16);

const newSlicedArray = arrayForNewElements.slice(1, 5);
const newEmptyArray = new Array(5);
newEmptyArray.fill('bang');
const arrayWithGun = newEmptyArray.map((element) => 'bim' + element);

// result:
console.log({ first, last });
console.log(newFilterdArray, 'filtered array');
console.log(newSlicedArray, 'sliced array');
console.log(newEmptyArray.join('-'), 'new empty array filed with "bang"');
console.log(arrayWithGun.join('-'));
console.log(': new array maped from "bang" array with more powerful weapon');
