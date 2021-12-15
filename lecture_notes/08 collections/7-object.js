'use strict';

const ages = {
  'Vasia Pupkin': 19,
  'Marcus Aurelius': 1860,
};
console.log({ ages });

ages['Vasia Pupkin'] = 20;
console.log({ ages });

Reflect.deleteProperty(ages, 'Vasia Pupkin');
console.log({ ages });

console.log({
  'Vasia Pupkin': Reflect.has(ages, 'Vasia Pupkin'),
  'Marcus Aurelius': Reflect.has(ages, 'Marcus Aurelius'),
});
