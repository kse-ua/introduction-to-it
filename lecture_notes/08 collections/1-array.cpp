#include <stdio.h>
#include <vector>
int main() {
  std::vector<int> ages = { 10, 12, 15, 15, 17, 18, 18, 19, 20 };

  ages.pop_back();
  ages.insert(ages.begin(), 4);
  ages.push_back(10);
  printf("first: %d\n", ages.at(0));
  printf("last: %d\n", ages.at(ages.size() - 1));
}
