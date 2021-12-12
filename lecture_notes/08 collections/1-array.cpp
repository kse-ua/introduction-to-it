#include <stdio.h>

int main() {
  int ages[] = { 10, 12, 15, 15, 17, 18, 18, 19, 20 };

  int first = ages[0];
  int length = sizeof(ages) / sizeof(ages[0]);
  int last = ages[length - 1];


  printf("first: %d\n", first);
  printf("last: %d\n", last);
}
