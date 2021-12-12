'use strict';

const ages = new Set([10, 12, 15, 15, 17, 18, 18, 19, 20]);
console.log({ ages });

ages.add(16);
ages.delete(20);

console.log({
  10: ages.has(10),
  16: ages.has(16),
  19: ages.has(19),
  20: ages.has(20),
});

ages.clear();
console.log({ ages });
