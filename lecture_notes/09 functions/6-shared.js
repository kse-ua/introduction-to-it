'use strict';

const cache = {};

const addProcedure = (a, b) => {
  const key = `${a}+${b}`;
  let res = cache[key];
  if (res !== undefined) return res;
  res = a + b;
  cache[key] = res;
  return res;
};

const subProcedure = (a, b) => {
  const key = `${a}-${b}`;
  let res = cache[key];
  if (res !== undefined) return res;
  res = a - b;
  cache[key] = res;
  return res;
};

console.log({ sub: subProcedure(5, 2) });
console.log({ add: addProcedure(5, 2) });
