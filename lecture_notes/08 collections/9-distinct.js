'use strict';

const distinct = (dataset) => {
    const keys = new Set();
    return dataset.filter((record) => {
        const cols = Object.keys(record).sort();
        const key = cols.map((field) => record[field]).join('\x00');
        const has = keys.has(key);
        if (!has) keys.add(key);
        return !has;
    });
};

// Usage

const flights = [
    { from: 'Kiev', to: 'Rome' },
    { from: 'Kiev', to: 'Warsaw' },
    { from: 'Dublin', to: 'Riga' },
    { from: 'Riga', to: 'Dublin' },
    { from: 'Kiev', to: 'Rome' },
    { from: 'Cairo', to: 'Paris' },
];

console.dir({ flights });

const directions = distinct(flights);

console.dir({ directions });
