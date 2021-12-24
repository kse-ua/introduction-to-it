'use strict';

// Antipattern: Premature optimization is the root of all evil D. Knuth
// Antipattern: Micro-optimization
{

  const range = (from, to) => {
    const arr = [];
    for (let i = from; i <= to; i++) arr.push(i);
    return arr;
  };

  const range2 = (from, to) => {
    if (to < from) return [];
    const len = to - from + 1;
    const range = new Array(len);
    for (let i = from; i <= to; i++) {
      range[i - from] = i;
    }
    return range;
  };

  const range3 = (from, to) => {
    if (to < from) return [];
    const len = to - from + 1;
    const range = new Array(len);
    let index = 0;
    for (let i = from; i <= to; i++) {
      range[index] = i;
      index++;
    }
    return range;
  };

  const range4 = (from, to) => {
    if (to < from) return [];
    const range = [0];
    range.length = to - from + 1;
    let index = 0;
    for (let i = from; i <= to; i++) {
      range[index] = i;
      index++;
    }
    return range;
  };

  const range5 = (from, to) => {
    if (to < from) return [];
    const len = to - from + 1;
    const range = new Array(len).fill(0);
    let index = 0;
    for (let i = from; i <= to; i++) {
      range[index] = i;
      index++;
    }
    return range;
  };

  // Micro-benchmarking utilities

  const rpad = (s, char, count) => (s + char.repeat(count - s.length));
  const lpad = (s, char, count) => (char.repeat(count - s.length) + s);
  const relativePercent = (best, time) => (time * 100n / best) - 100n;

  const benchmark = (count, args, tests) => {
    const times = tests.map((fn) => {
      const result = [];
      const begin = process.hrtime.bigint();
      for (let i = 0; i < count; i++) result.push(fn(...args));
      const end = process.hrtime.bigint();
      const diff = end - begin;
      const name = rpad(fn.name, '.', 22);
      const iterations = result.length;
      const log = [name, diff];
      console.log(log.join(' '));
      return { name, time: diff };
    });
    console.log();
    const top = times.sort((t1, t2) => Number(t1.time - t2.time));
    const best = top[0].time;
    top.forEach((test) => {
      test.percent = relativePercent(best, test.time);
      const time = lpad(test.time.toString(), '.', 10);
      const percent = test.percent === 0 ? 'min' : test.percent + '%';
      const line = lpad(percent, '.', 10);
      console.log(test.name + time + line);
    });
  };

  // Micro-benchmarking

  benchmark(
    1000000,
    [1, 100],
    [range, range2, range3, range4, range5]
  );

}
