#include<iostream>

std::string cities[] = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};

void f(std::string cities[]){
  int i = 0;
  int size = sizeof(*cities)/sizeof(cities);
  while (i <= size+1){
    std::cout << cities[i].length() << ", ";
    i++;
  }
  printf("\n");
}

void _print(std::string text, std::string cities[]){
  int i = 0;
  int size = sizeof(*cities)/sizeof(cities);
  if (text.size()>0){
    std::cout<<text;
  }
  while (i <= size+1){
    std::cout << cities[i] << ", ";
    i++;
  }
  printf("\n");
}

int f1(){
  std::string cities[] = {"Athens", "Roma"};
  _print("cities: ", cities); 
  return 0;
}



main(){
  f1();
  _print("cities: ", cities);  // external list of cities
  f(cities);
}
