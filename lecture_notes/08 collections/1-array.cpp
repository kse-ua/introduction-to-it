#include <stdio.h>
#include <vector>

int main() {
  std::vector<int> ages_1 = { 10, 12, 15, 15, 17, 18, 18, 19, 20 };
  ages_1.pop_back();
  ages_1.push_back(3);
  ages_1.insert(ages_1.begin(),3);


  printf("first: %d\n", ages_1.at(0));
  printf("last: %d\n", ages_1.at(ages_1.size() - 1));
}
