#include <stdio.h>

int * concat(int array1[], int array2[], int length1, int length2) {
  int length = length1 + length2;
  int* concated = new int[length];
  for (int i = 0; i < length1; i++) {
    concated[i] = array1[i];
  };

  for (int i = 0; i < length2; i++) {
    concated[i + length1] = array2[i];
  };
  
  return concated;
};

int main() {
  int schoolAges[] = { 10, 12, 15, 15 };
  int studentAges[] = { 17, 18, 18, 19, 20 };

  int schoolLength = sizeof(schoolAges) / sizeof(int);
  int studentLength = sizeof(studentAges) / sizeof(int);
  int length = schoolLength + studentLength;
  int* ages = concat(schoolAges, studentAges, schoolLength, studentLength);

  for (int i = 0; i < length; i++) {
    printf("ages[%d]: %d\n", i, ages[i]);
  };
};
