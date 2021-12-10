#include<iostream>

const int max(int a = 0,int b = 0){
  if (a > b)
    return a;
  else
    return b;      
}


main() { 
  int _max[] = {max(10, 20), max(10), max(-20)};
  int i = 0;
  int size = sizeof(_max) / sizeof(int);  // array size
  while (i <= size){
    std::cout << _max[i] << " ";
    i++;
  }
}
