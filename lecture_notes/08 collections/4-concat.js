// Exaple CONTACT
const ArrLowerCase1 = ['h', 'e', 'l', 'l', 'o'];
const ArrLowerCase2 = ['w', 'o', 'r', 'l', 'd'];

const UpperCase1 = ArrLowerCase1.map(name => name.toUpperCase());
const UpperCase2 = ArrLowerCase2.map(name => name.toUpperCase());

console.log(UpperCase1.concat(UpperCase2)); // ["H", "E", "L", "L", "O", "W", "O", "R", "L", "D"]

