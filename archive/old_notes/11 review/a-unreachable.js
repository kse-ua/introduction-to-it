'use strict';

// Antipattern: Unreachable code
// linter detectable
{
  const isValid = (name) => {
    return true;
    // everything after return is unreachable
    if (name.includes(' ')) return false;
  };

  console.log(isValid('Marcus Aurelius'));
}

// Antipattern: Unreachable code
// run-time or analytic
{
  const isValid = (name) => {
    if (!name) return false;
    if (name.length === 0) return false;
    if (name.includes(' ')) return false;
    if (name[0] === ' ') return false; // unreachable
    return true;
  };

  console.log(isValid('Marcus Aurelius'));
}
