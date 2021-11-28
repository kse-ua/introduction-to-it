'use strict';

const counter = {
  value: 0,
  inc(x) {
    this.value += x;
  },
};

counter.inc(10);
console.log({ counter });

counter.inc(20);
console.log({ counter });
