#'use strict';

#const distinct = (dataset) => {
#  const keys = new Set();
#  return dataset.filter((record) => {
#    const cols = Object.keys(record).sort();
#    const key = cols.map((field) => record[field]).join('\x00');
#    const has = keys.has(key);
#    if (!has) keys.add(key);
#    return !has;
#  });
# };

#// Usage

# const flights = [
#  { from: 'Kiev', to: 'Rome' },
#  { from: 'Kiev', to: 'Warsaw' },
#  { from: 'Dublin', to: 'Riga' },
#  { from: 'Riga', to: 'Dublin' },
#  { from: 'Kiev', to: 'Rome' },
#  { from: 'Cairo', to: 'Paris' },
# ];

# console.dir({ flights });
# const directions = distinct(flights);
# console.dir({ directions });

# ---------------------------------------------------------------

flights_from = ['Kiev', 'Kiev', 'Dublin', 'Riga', 'Kiev', 'Cairo']
flights_to = ['Rome', 'Warsaw', 'Riga', 'Dublin', 'Rome', 'Paris']
flights = [flights_from[x] + ' >> ' + flights_to[x] for x in range(len(flights_from))]
print('flights :', '\n', flights)
directions = list(dict.fromkeys(flights))
print('directions :', '\n', directions)

