'use strict';

// Antipattern: Dead code
{
  const isValid = (name) => {
    const parts = name.split(' ');
    if (parts.length > 0) parts.push('Last');
    else parts.unshift('First');
    return true;
  };

  console.log(isValid('Marcus Aurelius'));
}
