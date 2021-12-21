'use strict';

// Antipattern: Nested loops
// Antipattern: Pyramid of doom
{
  const phones = [
    { name: 'Marcus', phone: '12345678' },
    { name: 'Kant', phone: '1234567' },
  ];

  const cities = [
    { name: 'Marcus', city: 'Roma' },
    { name: 'Kant', city: 'Kaliningrad' },
  ];

  const prefixes = [
    { name: 'Roma', prefix: '+3906' },
    { name: 'Kaliningrad', prefix: '+7401' },
  ];

  const getPhoneNumber = (name) => {
    for (const record1 of phones) {
      if (record1.name === name) {
        for (const record2 of cities) {
          if (record2.name === name) {
            for (const record3 of prefixes) {
              if (record3.name === record2.city) {
                return record3.prefix + record1.phone;
              }
            }
          }
        }
      }
    }
  };

  const callMarcus = getPhoneNumber('Marcus');
  console.dir({ callMarcus });
}

// Antipattern: Hidden loops
{
  const persons = [
    { name: 'Marcus', phone: '12345678', city: 'Roma' },
    { name: 'Kant', phone: '1234567', city: 'Kaliningrad' },
  ];

  const prefixes = {
    Roma: '+3906',
    Kaliningrad: '+7401',
  };

  const getPhoneNumber = (name) => {
    const person = persons.find((person) => person.name === name);
    const { phone, city } = person;
    const prefix = prefixes[city];
    return prefix + phone;
  };

  const callMarcus = getPhoneNumber('Marcus');
  console.dir({ callMarcus });
}

// Solution
{
  const persons = {
    Marcus: { name: 'Marcus', phone: '12345678', city: 'Roma' },
    Kant: { name: 'Kant', phone: '1234567', city: 'Kaliningrad' },
  };

  const prefixes = {
    Roma: '+3906',
    Kaliningrad: '+7401',
  };

  const getPhoneNumber = (name) => {
    const person = persons[name];
    const { phone, city } = person;
    const prefix = prefixes[city];
    return prefix + phone;
  };

  const callMarcus = getPhoneNumber('Marcus');
  console.dir({ callMarcus });
}
