'use strict';

let ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];

// Implementation
function onlyDistinct(value, index, self) {
    return self.indexOf(value) === index;
}

// Usage
ages = ages.filter(onlyDistinct);

ages.unshift(8)
ages.push(22)

const first = ages[0];
const last = ages[ages.length - 1];

console.log({ first, last });
