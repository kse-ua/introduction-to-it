'use strict';

const addFunction = (a, b) => {
  const res = a + b;
  return res;
};

const cache = {};

const addProcedure = (a, b) => {
  const key = `${a},${b}`;
  let res = cache[key];
  if (res !== undefined) return res;
  res = a + b;
  cache[key] = res;
  return res;
};

console.log([
  addFunction(10, 20),
  addFunction(1, 2),
  addFunction(100, 20),
  addFunction(100, 200),
]);

console.log([
  addProcedure(10, 20),
  addProcedure(1, 2),
  addProcedure(100, 20),
  addProcedure(100, 200),
]);
