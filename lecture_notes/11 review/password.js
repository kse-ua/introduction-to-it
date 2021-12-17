// Generate random password

const GeneratePassword = (alphabet = 'abc123', length = 7) =>  {
  let key = '';
  for ( let i = 0; i < length; i++ ){
    const Index = Math.floor(Math.random() * alphabet?.length);
    key += alphabet?.[Index];
  };
  return key
};

const result = GeneratePassword('abc123', 7); // Random password for 7 characters using 'abc123' (1)
console.log(Random('abc', 9)); // Random password for 9 characters using 'abc'
console.log(Random()); // Random password for 7 characters using 'abc123'
console.log(result); // Variable 'result' (1)
