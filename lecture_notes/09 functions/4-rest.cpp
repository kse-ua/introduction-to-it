#include<iostream>
#include<typeinfo>

const void f2(auto arg){  // auto allows you not to specify the type of a variable
      std::cout << arg << "\n";
      std::cout << typeid(arg).name() << "\n";  // typeid
}


main(){
  f2(1);
  f2("Marcus");
  f2({'field': 'value'});
}
