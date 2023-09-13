'use strict';

// Antipattern: Spaghetti code
// - JMP, GOTO
// - Callbacks
// - Events
// - Promises

// Callbacks
{
  const invoke = (validate, fn, a, b, callback) => {
    const result = fn(validate, a, b);
    callback(null, result);
  };

  const max = (validate, a, b) => {
    let valid = true;
    const conjunction = (err, res) => {
      valid = valid && res;
    };
    validate(a, conjunction);
    validate(b, conjunction);

    if (!valid) throw new TypeError('Unexpected parameter');

    return Math.max(a, b);
  };

  const isNumber = (value, callback) => {
    const valid = typeof value === 'number';
    callback(null, valid);
  };

  invoke(isNumber, max, 10, 20, (err, result) => {
    console.dir({ result });
  });
}

// Events
// Try to debug this code to find logical error
{
  const { EventEmitter } = require('events');

  const incoming = new EventEmitter();
  const controller = new EventEmitter();
  const processing = new EventEmitter();

  const parameters = [];

  incoming.on('return', (result) => {
    console.dir({ result });
  });

  processing.on('max', (a, b) => {
    incoming.emit('return', Math.max(a, b));
  });

  controller.on('parameter', (value) => {
    parameters.push(value);
  });

  incoming.on('input', (data) => {
    if (typeof data === 'string') {
      controller.emit('call', data);
    } else {
      controller.emit('parameter', data);
    }
  });

  controller.on('call', (name) => {
    processing.emit(name, ...parameters);
  });

  incoming.emit('input', 10);
  incoming.emit('input', 20);
  incoming.emit('input', 'max');
}
