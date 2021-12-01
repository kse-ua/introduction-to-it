let ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
ages.splice(4, 1);
let first = ages[0];
let last = ages[-1];
ages.splice(4, 1);
ages.splice(5, 1, 'Boomer')
ages.push('Alex')
ages.shift()
ages.unshift('Start')
console.log({first, last});
console.log(ages)
