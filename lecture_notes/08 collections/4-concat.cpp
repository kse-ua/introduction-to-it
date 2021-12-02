#include <stdio.h>

void concat_and_print(int arr1[], int arr2[], int len1, int len2){
  // int len1 = sizeof(arr1) / sizeof(int);
  // int len2 = sizeof(arr2) / sizeof(int);
  int concated_arr[len1 + len2];

  for (int i = 0; i < len1; i++) {
    concated_arr[i] = arr1[i];
    printf("concated_arr[%d]: %d\n", i, concated_arr[i]);
  }

  for (int i = 0; i < len1; i++) {
    concated_arr[i + len1] = arr2[i];
    printf("concated_arr[%d]: %d\n", i+len1, concated_arr[i+len1]);
  }
}


int main() {
  int schoolAges[] = { 10, 12, 15, 15 };
  int studentAges[] = { 17, 18, 18, 19, 20 };

  int schoolLength = sizeof(schoolAges) / sizeof(int);
  int studentLength = sizeof(studentAges) / sizeof(int);

  concat_and_print(schoolAges, studentAges, schoolLength, studentLength);
}
