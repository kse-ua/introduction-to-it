#include <stdio.h>

int MAX_PURCHASE = 2000;

int calculateTotal(int prices[], int length) {
  int amount = 0;
  for (int i = 0; i < length; i++) {
    amount += prices[i];
  }
  return amount;
}

// Usage

int main() {
  int purchase[] = { 1500, 100, 10, 50 };

  int length = sizeof(purchase) / sizeof(int);
  int total = calculateTotal(purchase, length);

  if (total <= MAX_PURCHASE) {
    printf("%d\n", total);
  }
}
