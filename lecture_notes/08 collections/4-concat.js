'use strict';

const schoolAges = [10, 12, 15, 15];
const studentAges = [17, 18, 18, 19, 20];

// Create a total array
let primes = schoolAges.concat(studentAges);

// Declaring a func, which return first and last elem

function FirstandLastElem() {   

   let first=primes[0];
   let last=primes[primes.length-1]; 
      
   console.log({ first, last });

  } 
  
  FirstandLastElem();
