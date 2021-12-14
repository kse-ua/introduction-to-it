#include <iostream>
using namespace std;
#include <tuple>

int get_first_and_last(int array[], int length) {
  int first = array[0];
  int last = array[length - 1];
  tuple <int, int> result(int num1, int num2)
  return make_tuple(first, last);
}

int main() {
  int ages[] = { 10, 12, 15, 15, 17, 18, 18, 19, 20 };
  int length = sizeof(ages[]) / sizeof(int);
  int first, last;
  tie(first, last) = get_first_and_last(ages[9], length);
  printf("result: %d\n", first, " ", last);
}
