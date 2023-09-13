#include <stdio.h>

int main() {
  int schoolAges[] = { 10, 12, 15, 15 };
  int studentAges[] = { 17, 18, 18, 19, 20 };

  int schoolLength = sizeof(schoolAges) / sizeof(int);
  int studentLength = sizeof(studentAges) / sizeof(int);
  int length = schoolLength + studentLength;
  int ages[length];

  for (int i = 0; i < schoolLength; i++) {
    ages[i] = schoolAges[i];
  }

  for (int i = 0; i < studentLength; i++) {
    ages[i + schoolLength] = studentAges[i];
  }

  for (int i = 0; i < length; i++) {
    printf("ages[%d]: %d\n", i, ages[i]);
  }
}
