'use strict';

const addFunction = (a, b) => {
  const res = a + b;
  return res;
};

const subFunction = (a, b) => {
  const res = a - b;
  return res;
};

const addProcedure = (a, b) => {
  const key = `${a},${b}`;
  let res = addProcedure.cache[key];
  if (res) return res;
  res = a + b;
  addProcedure.cache[key] = res;
  return res;
};

addProcedure.cache = {};

const subProcedure = (a, b) => {
  const key = `${a},${b}`;
  let res = subProcedure.cache[key];
  if (res) return res;
  res = a - b;
  subProcedure.cache[key] = res;
  return res;
};

subProcedure.cache = {};

const test = (cases) => {
  const results = {};
  for (const element of cases) {
    const [f, args, res] = element;
    const result = f(...args);
    const key = `${f.name}(${args})`;
    results[key] = result === res;
  }
  console.table(results);
};

test([
  [addProcedure, [1, 2], 3],
  [addProcedure, [100, 20], 120],
  [addProcedure, [100, 200], 300],
  [subProcedure, [5, 2], 3],
  [addProcedure, [5, 2], 7],
]);

test([
  [addFunction, [1, 2], 3],
  [addFunction, [100, 20], 120],
  [addFunction, [100, 200], 300],
  [subFunction, [5, 2], 3],
  [addFunction, [5, 2], 7],
]);
