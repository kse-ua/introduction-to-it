using namespace std;
#include <iostream>

int main() {
  int *ages = new int[9]{ 10, 12, 15, 15, 17, 18, 18, 19, 20 };

  int first = ages[0];
  int length = 8;
  int last = ages[length];


  cout << first << endl;
  cout << last << endl;
  delete[] ages;
}
