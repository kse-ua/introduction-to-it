'use strict';

// Antipattern: Cryptic code

const emitter = (l, o) => (l = {}, o = {
  on: (n, f) => (l[n] = l[n] || []).push(f),
  emit: (n, ...d) => (l[n] || []).map((f) => f(...d)),
  once: (n, f, g) => o.on(n, g = (...a) => (f(...a), o.remove(n, g))),
  remove: (n, f, e) => (e = l[n] || [], e.splice(e.indexOf(f), 1)),
  clear: (n) => (n ? delete l[n] : l = {}),
  count: (n) => (l[n] || []).length,
  listeners: (n) => (l[n] || []).slice(),
  names: () => Object.keys(l)
});

// Usage

const ee = emitter();

ee.on('e1', (data) => {
  console.dir(data);
});

ee.emit('e1', { msg: 'e1 ok' });
