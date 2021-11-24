#include <stdio.h>
#include <string>

int sum(int argument[], int length) {
  int output = 0;
  for(int i = 0; i < length; i++){
    output += argument[i];
  }
  return output;
}

int main() {
  int test_input[] = {1, 3, 5, 7, 9};
  int length = sizeof(test_input) / sizeof(int);
  std::string output = std::to_string(sum(test_input, length));
  printf(output.c_str());
}
