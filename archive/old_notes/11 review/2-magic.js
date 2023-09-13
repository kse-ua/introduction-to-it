'use strict';

// Antipattern: Magic number
{
  const name = 'Marcus Aurelius';
  const result = name.padStart(17);
  console.log(result);
}

// Solution
{
  const NAME_LENGTH = 17;
  const name = 'Marcus Aurelius';
  const result = name.padStart(NAME_LENGTH);
  console.log(result);
}

// Solution
{
  const PAD_LENGTH = 2;
  const name = 'Marcus Aurelius';
  const result = name.padStart(name.length + PAD_LENGTH);
  console.log(result);
}

// Solution
{
  const config = require('./config.js');
  const name = 'Marcus Aurelius';
  const result = name.padStart(config.name.lenght);
  console.log(result);
}

// Antipattern: : Magic string
{
  const pos = '\x1b[2;10H';
  console.log(pos);
}

// Solution
{
  const pos = (row, col) => console.log(`\x1b[${row};${col}H`);
  pos(2, 10);
}

// Exception
{
  const name = 'Marcus Aurelius';
  for (let i = 0; i < name.length; i++) {
    console.log(i, name[i]);
  }
}

// Exception
{
  const last = (array) => array[array.length - 1];
  const array = ['A', 'B', 'C'];
  console.log(last(array));
}
