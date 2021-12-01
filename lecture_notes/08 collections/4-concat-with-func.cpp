#include <iostream>

void sumArray(int m,int n,int array1[],int array2[]){
    int arr[m + n];
    for (int i = 0; i < m + n; i++)
    {
        if (i < m) {
            arr[i] = array1[i];
        }
        else {
            arr[i] = array2[i - m];
        }
    }
    for (int i = 0; i < m + n; i++) {
        std::cout << arr[i] << ' ';
    }
    for (int i = 0; i < m+n; i++) {
    printf("ages[%d]: %d\n", i, arr[i]);
  }
}
int main() {
  int schoolAges[] = { 10, 12, 15, 15 };
  int studentAges[] = { 17, 18, 18, 19, 20 };
  int schoolLength = sizeof(schoolAges) / sizeof(int);
  int studentLength = sizeof(studentAges) / sizeof(int);
  sumArray(schoolLength,studentLength,schoolAges,studentAges);

}
