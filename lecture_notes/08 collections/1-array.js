"use strict";

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const firstElement = 5,
  secondElement = 10;
ages.pop();
ages.push(firstElement, secondElement);
ages.shift();
ages.unshift(firstElement);

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });
