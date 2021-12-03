// PUSH
'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
const total = ages.push(21, 21, 22);

console.log(ages); // [10, 12, 15, 15, 17, 18, 18, 19, 20, 21, 21, 22]


// POP
'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
const popped  = ages.pop();

console.log(ages); // [10, 12, 15, 15, 17, 18, 18, 19]


// UNSHIFT
'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
ages.unshift(8, 9); 

console.log(ages); // [8, 9, 10, 12, 15, 15, 17, 18, 18, 19, 20]


// SHIFT
'use strict';

const ages = [10, 12, 15, 15, 17, 18, 18, 19, 20];
const shifted =  ages.shift(); 

console.log(ages); // [12, 15, 15, 17, 18, 18, 19, 20]

// EXAMPLE
let cats = ['Mary', 'Biba'];

cats.push('Boba', 'Tod'); 
console.log(cats) // ["Mary", "Biba", "Boba", "Tod"]

cats.pop(); 
console.log(cats) // ["Mary", "Biba", "Boba"]

cats.shift();
console.log(cats) // ["Biba", "Boba"]

cats.unshift('Mary', 'Meow');
console.log(cats) // ["Mary", "Meow", "Biba", "Boba"]
