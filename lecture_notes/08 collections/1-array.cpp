#include <stdio.h>
#include <vector>

int main() {
  std::vector< int > ages;
  int ageses[] = { 10, 12, 15, 15, 17, 18, 18, 19, 20 };

  int add_last = 21;
  int add_first = 9;
  ages.push_back(add_last);

  int first_after_add = ages[0];
  int length = sizeof(ages) / sizeof(ages[0]);
  int last_after_add = ages[length - 1];

  printf("first: %d\n", first_after_add);
  printf("last: %d\n", last_after_add);
}
