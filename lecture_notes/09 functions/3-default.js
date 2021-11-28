'use strict';

const max = (a = 0, b = 0) => (a > b ? a : b);

console.log([max(10, 20), max(10), max(-20)]);
