//#include <stdio.h>
#include <iostream>
using namespace std;

void printArray(int *array, int size)
{
  for (int i = 0; i < size; i++)
  {
    printf("%d ", array[i]);
  }
  printf("\n");
}

int *addDelete(int num1, int num2, int array[], int sizeArray, int *allAges)
{
  for (int i = 0; i < sizeArray; i++)
  {
    allAges[i] = array[i];
  }

  allAges[sizeArray] = num2; //add num to the end
  sizeArray++;               //add num => size = size +1
  printArray(allAges, sizeArray);

  allAges[sizeArray] = 0;
  sizeArray--;
  printArray(allAges, sizeArray);

  for (int i = sizeArray; i > 0; i--)
  {
    allAges[i] = allAges[i - 1];
  }
  allAges[0] = num1;
  //sizeArray = sizeArray + 1;
  printArray(allAges, ++sizeArray);

  for (int i = 1; i <= sizeArray; i++)
  {
    allAges[i - 1] = allAges[i];
  }
  //sizeArray = sizeArray -1;
  printArray(allAges, --sizeArray);

  return allAges;
}

int main()
{
  int ages[] = {10, 12, 15, 15, 17, 18, 18, 19, 20};

  int first = ages[0];
  int length = sizeof(ages) / sizeof(ages[0]);
  int last = ages[length - 1];
  printf("first: %d\n", first);
  printf("last: %d\n", last);
  int allAges[50] = {}; // standard of c++ doesn't allow allAges[length]

  addDelete(9, 21, ages, length, allAges);
  cout << "The result is: ";
  printArray(allAges, length);
}
