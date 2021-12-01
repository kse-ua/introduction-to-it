'use strict';

const ages = new Map();

ages.set('Vasia Pupkin', 19);
ages.set('Marcus Aurelius', 1860);
console.log({ ages });

ages.set('Vasia Pupkin', 20);
console.log({ ages });

ages.delete('Vasia Pupkin');
console.log({ ages });

console.log({
  'Vasia Pupkin': ages.has('Vasia Pupkin'),
  'Marcus Aurelius': ages.has('Marcus Aurelius'),
});

ages.clear();
console.log({ ages });

# Python version
ages = {}

ages["Vasia Pupkin"] = 19
ages['Marcus Aurelius'] = 1860
print(f"ages: {ages}")

ages["Vasia Pupkin"] = 20
print(f"ages: {ages}")

print("Vasia Pupkin:", "Vasia Pupkin" in ages)
print('Marcus Aurelius:', "Marcus Aurelius" in ages)

ages.clear()
print(f"ages: {ages}")
