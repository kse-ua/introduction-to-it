'use strict';

// Antipattern: Fool-proof code
// Assumption: idiots will pass anything to my function
{
  const max = (...args) => {
    if (args.length !== 2) {
      throw new Error('Function expects two aruments');
    }
    const a = args.shift();
    if (typeof a !== 'number') {
      throw new Error('Unexpected type of first arument');
    }
    const b = args.shift();
    if (typeof b !== 'number') {
      throw new Error('Unexpected type of second arument');
    }
    return a > b ? a : b;
  };

  // Usage 1
  console.log(`Max of 10 and 20 is ${max(10, 20)}`);

  // Usage 2
  const a = new Number(10);
  const b = new Number(20);
  console.log(`Max of ${a} and ${b} is ${max(a, b)}`);

  // Usage 3
  const x = {
    [Symbol.toPrimitive]() {
      return 10;
    }
  };
  const y = 20;
  console.log(`Max of ${x} and ${y} is ${max(x, y)}`);
}

// Solution
{
  const max = (a, b) => (a > b ? a : b);

  // Usage 1
  console.log(`Max of 10 and 20 is ${max(10, 20)}`);

  // Usage 2
  const a = new Number(10);
  const b = new Number(20);
  console.log(`Max of ${a} and ${b} is ${max(a, b)}`);

  // Usage 3
  const x = {
    [Symbol.toPrimitive]() {
      return 10;
    }
  };
  const y = 20;
  console.log(`Max of ${x} and ${y} is ${max(x, y)}`);
}
