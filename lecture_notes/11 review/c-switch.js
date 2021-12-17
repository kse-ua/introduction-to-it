'use strict';

// Antipattern: switch
{
  const color = (name) => {
    switch (name) {
    case 'black':
      console.log(1);
      break;
    case 'red':
      console.log(2);
      break;
    case 'green':
      console.log(3);
      break;
    case 'yellow':
      console.log(4);
      break;
    case 'blue':
      console.log(5);
      break;
    case 'magenta':
      console.log(6);
      break;
    case 'cyan':
      console.log(7);
      break;
    case 'white':
      console.log(8);
      break;
    }
    console.log('color name:', name);
  };

  color('white');
}

// Better switch ussage
{
  const color = (name) => {
    switch (name) {
    case 'black': return 1;
    case 'red': return 2;
    case 'green': return 3;
    case 'yellow': return 4;
    case 'blue': return 5;
    case 'magenta': return 6;
    case 'cyan': return 7;
    case 'white': return 8;
    }
  };

  console.log('white', color('white'));
}

// Use array instead
{
  const COLORS = [
    /* 1 */ 'black',
    /* 2 */ 'red',
    /* 3 */ 'green',
    /* 4 */ 'yellow',
    /* 5 */ 'blue',
    /* 6 */ 'magenta',
    /* 7 */ 'cyan',
    /* 8 */ 'white',
  ];
  const color = (name) => COLORS.indexOf(name) + 1;

  console.log('white', color('white'));
}

// Use object instead
{
  const COLORS = {
    black: 1,
    red: 2,
    green: 3,
    yellow: 4,
    blue: 5,
    magenta: 6,
    cyan: 7,
    white: 8,
  };
  const color = (name) => COLORS[name];

  console.log('white', color('white'));
}

// Use Map instead
{
  const COLORS = new Map([
    ['black', 1],
    ['red', 2],
    ['green', 3],
    ['yellow', 4],
    ['blue', 5],
    ['magenta', 6],
    ['cyan', 7],
    ['white', 8],
  ]);
  const color = (name) => COLORS.get(name);

  console.log('white', color('white'));
}
