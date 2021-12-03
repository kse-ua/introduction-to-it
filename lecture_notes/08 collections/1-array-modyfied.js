'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });

const array_for_new_elements = ages.reverse();
console.log(array_for_new_elements);
array_for_new_elements.pop();
array_for_new_elements.push("new last element");
array_for_new_elements.shift();
array_for_new_elements.unshift("new first element");
console.log(array_for_new_elements);
console.log(array_for_new_elements.filter(element => element > 16 || element === 12),"filtered array")

const sliced_array = array_for_new_elements.slice(1,5);
console.log(sliced_array);
console.log(sliced_array.includes(18));

const new_empty_array = new Array(5);
new_empty_array.fill("bang");
console.log(new_empty_array);
console.log(new_empty_array.join("-"));

const array_with_gun = new_empty_array.map(element => "bim" + element)
console.log(array_with_gun.join(""));
