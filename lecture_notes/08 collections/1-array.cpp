//#include <stdio.h>
#include <iostream>
using namespace std;

void printArray(int* array, int size){  
  for (int i = 0; i < size; i++)
  {
    printf("%d ", array[i]);
  }
  printf("\n");
}

int* addDelete(int num1, int num2, int array[], int sizeAges)
{
  int allAges[50] = {};
  for (int i = 0; i < sizeAges; i++) {
    allAges[i] = array[i];
  }
  
  allAges[sizeAges] = num2;
  sizeAges++;
  printArray(allAges, sizeAges);

  allAges[sizeAges] = 0;
  sizeAges--;
  printArray(allAges, sizeAges);
  
  allAges[sizeAges] = num1;
  printArray(allAges, sizeAges);
  
  allAges[sizeAges] = 0;
  printArray(allAges, sizeAges);
  return 0;
}

int main()
{
  int ages[] = {10, 12, 15, 15, 17, 18, 18, 19, 20};
  
  int first = ages[0];
  int length = sizeof(ages) / sizeof(ages[0]);
  int last = ages[length - 1];
  printf("first: %d\n", first);
  printf("last: %d\n", last);
  int* z = addDelete(9, 21, ages, length);
  cout << "The result is " << z << "\n";
}
