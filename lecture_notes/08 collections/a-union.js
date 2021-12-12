'use strict';

const union = (s1, s2) => {
  const ds = s1.slice(0);
  for (let i = 0; i < s2.length; i++) {
    const item = s2[i];
    if (!ds.includes(item)) ds.push(item);
  }
  return ds;
};

// const union = (s1, s2) => new Set([...s1, ...s2]);

// Usage

const cities1 = ['Beijing', 'Kiev'];
const cities2 = ['Kiev', 'London', 'Baghdad'];
console.dir({ cities1, cities2 });

const results = union(cities1, cities2);
console.dir(results);
