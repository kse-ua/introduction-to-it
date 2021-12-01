// Implementation

const getFirstAndLast = (array) => ({
    first: array[0],
    last: array[array.length - 1],
});

// Usage

const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];
const ages = (schoolAges.concat(studentAges));
const result = getFirstAndLast(ages);
console.log(result);
