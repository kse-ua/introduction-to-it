'use strict';

function add1(a, b) {
  return a + b;
}

const add2 = function (a, b) {
  return a + b;
};

const add3 = (a, b) => {
  const res = a + b;
  return res;
};

const add4 = (a, b) => a + b;

console.log({
  add1: add1(10, 20),
  add2: add2(10, 20),
  add3: add3(10, 20),
  add4: add4(10, 20),
});
