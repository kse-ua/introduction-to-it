'use strict';

const cache = {};

const addProcedure = (a, b) => {
  const key = `${a},${b}`;
  let res = cache[key];
  if (res) return res;
  res = a + b;
  cache[key] = res;
  return res;
};

const subProcedure = (a, b) => {
  const key = `${a},${b}`;
  let res = cache[key];
  if (res) return res;
  res = a - b;
  cache[key] = res;
  return res;
};

const test = (f, args, res) => {
  const result = f(...args);
  if (result === res) return true;
  else return false;
};

console.log([
  test(addProcedure, [1, 2], 3),
  test(addProcedure, [100, 20], 120),
  test(addProcedure, [100, 200], 300),
  test(subProcedure, [5, 2], 3),
  test(addProcedure, [5, 2], 7),
]);
