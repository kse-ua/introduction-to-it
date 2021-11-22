'use strict';

const difference = (s1, s2) => {
  const ds = [];
  for (let i = 0; i < s1.length; i++) {
    const item = s1[i];
    if (!s2.includes(item)) ds.push(item);
  }
  return ds;
};

// Usage

const cities1 = ['Beijing', 'Kiev'];
const cities2 = ['Kiev', 'London', 'Baghdad'];
console.dir({ cities1, cities2 });

const results = difference(cities1, cities2);
console.dir(results);
