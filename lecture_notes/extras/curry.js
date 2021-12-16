'use strict';

// Implementation

const curry = (fn) => function curried(...args) {
  if (fn.length > args.length)
    return (...args2) => curried(...args, ...args2);
  else
    return fn(...args);
};

// Usage

const sum4 = (a, b, c, d) => (a + b + c + d);

const f = curry(sum4);
const y1 = sum4(1, 2, 3, 4);
const y2 = f(1, 2, 3, 4);
const y3 = f(1, 2, 3)(4);
const y4 = f(1, 2)(3)(4);
const y5 = f(1)(2)(3)(4);
const y6 = f(1)(2, 3, 4);
const y7 = f(1)(2)(3, 4);
const y8 = f(1, 2)(3, 4);

console.log(y1, y2, y3, y4, y5, y6, y7, y8);
