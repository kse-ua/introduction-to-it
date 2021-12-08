#include <iostream>

struct Ints {
  int firstEl;
  int lastEl;
};

Ints getFirstAndLast(int *array, int lengthArray) {
  Ints res = Ints();
  res.firstEl = array[0];
  res.lastEl = array[lengthArray - 1];
  return res;
};

int main(int argc, char const *argv[]) {
  int ages[] = {10, 12, 15, 15, 17, 18, 18, 19, 20};
  int lengthAges = sizeof(ages) / sizeof(int);
  Ints z = getFirstAndLast(ages, lengthAges);
  printf("'first': %d, 'last': %d", z.firstEl, z.lastEl);
  return 0;
}
