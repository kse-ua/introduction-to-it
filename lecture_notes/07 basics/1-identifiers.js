'use strict';

const MAX_PURCHASE = 2000;

const calculateTotal = (prices) => {
  let amount = 0;
  for (const price of prices) {
    amount += price;
  }
  return amount;
};

// Usage

const purchase = [1500, 100, 10, 50];
const total = calculateTotal(purchase);
if (total <= MAX_PURCHASE) {
  console.log({ total });
}
