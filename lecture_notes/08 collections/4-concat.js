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
const greeting = ['h', 'e', 'l', 'l', 'o',' '];
const target = ['w', 'o', 'r', 'l', 'd'];

const toUpper = (name) => name.toUpperCase();

const preparedGreeating = greeting.map(toUpper);
const preparedTarget = target.map(toUpper);

console.log(preparedGreeating.concat(preparedTarget).join(''));

