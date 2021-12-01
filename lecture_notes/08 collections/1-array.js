'use strict';

let ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

// To add elements in the beginning and at the end of an array
ages.unshift(9)
ages.push(21);
// console.log(ages)
var firstAfterAdd = ages[0];
var lastAfterAdd = ages[ages.length - 1];

console.log({ firstAfterAdd, lastAfterAdd });

// To delete items in the beginning of an array and at the end of it
ages.shift();
ages.pop();
// console.log(ages);
var firstAfterDeletion = ages[0];
var lastAfterDeletion = ages[ages.length - 1];

console.log({ firstAfterDeletion, lastAfterDeletion });
