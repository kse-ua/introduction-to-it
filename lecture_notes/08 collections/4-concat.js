const getFirstAndLast = (array) => ({
  first: array[0],
  last: array[array.length - 1],
});

const concat = (arr1, arr2) => {
  const arr = arr1.slice();
  arr.push(...arr2);
  return arr;
};

const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];
const ages = concat(schoolAges, studentAges);
const { first, last } = getFirstAndLast(ages);
console.log({ first, last });


// Exaple CONTACT
const ArrLowerCase1 = ['h', 'e', 'l', 'l', 'o'];
const ArrLowerCase2 = ['w', 'o', 'r', 'l', 'd'];

const UpperCase1 = ArrLowerCase1.map(name => name.toUpperCase());
const UpperCase2 = ArrLowerCase2.map(name => name.toUpperCase());

console.log(UpperCase1.concat(UpperCase2)); // ["H", "E", "L", "L", "O", "W", "O", "R", "L", "D"]

