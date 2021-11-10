# Implementation

MAX_PURCHASE = 2000

def calculateTotal(prices):
  amount = 0
  for i in prices:
    amount = amount + i
  return amount

# Usage

purchase = [1500, 100, 10, 50]
total = calculateTotal(purchase)
if total <= MAX_PURCHASE:
  print(total)
