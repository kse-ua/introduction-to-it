// Generate random integer value in given range
const Random = (min = 0, max = 100) =>  min + Math.floor(Math.random() * (max - min + 1));

const result = Random(1, 9); // Variable 'result' will equal for random number in the range [1 - 9] (1)
console.log(Random(1, 9)); // Random number in the range [1 - 9] (2)
console.log(Random()); // Random number in the range [0 - 100] (2)
console.log(result); // Variable 'result' (1)
