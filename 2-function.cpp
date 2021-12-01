#include <array>
#include <iostream>
using namespace std;

int main(){
  array<int,9> values {10, 12, 15, 15, 17, 18, 18, 19, 20};

  cout<<"First element is: "<<values.front()<<endl; //.front() & .back() option
  cout<<"Last element is:  "<<values.back()<<endl;

  return 0;
}
