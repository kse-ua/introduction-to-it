'use strict';

// Antipattern: Copy and paste

// Google: javascript get first element of array
// First result:
// https://stackoverflow.com/questions/4090491/get-first-element-in-array

// I tried this. But it would return [object Object].
{
  alert($(ary).first());
}

// Approved
{
  alert(ary[0])
}

// Patch built-in class
{
  Array.prototype.first = function() {
    return this[0];
  };
}

// Another solution
{
  array.find((e) => !!e);
}
