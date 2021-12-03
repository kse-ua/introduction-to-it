'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });

const arrayForNewElements = ages.reverse();
console.log(arrayForNewElements);
arrayForNewElements.pop();
arrayForNewElements.push('new last element');
arrayForNewElements.shift();
arrayForNewElements.unshift('new first element');
console.log(arrayForNewElements);
arrayForNewElements.filter((element) =>
  element > 16 || element === 12);
console.log(arrayForNewElements, 'filtered array');
const newSlicedArray = arrayForNewElements.slice(1, 5);
console.log(newSlicedArray);
console.log(newSlicedArray.includes(18));

const newEmptyArray = new Array(5);
newEmptyArray.fill('bang');
console.log(newEmptyArray);
console.log(newEmptyArray.join('-'));

const arrayWithGun = newEmptyArray.map((element) => 'bim' + element);
console.log(arrayWithGun.join(''));
