#include <string>
#include <vector>
#include <algorithm>
// use C++ of standard 11
// version	description
// C++98	C++ 1998/2003 Standard
// C++11	C++ 2011 Standard
// C++14	C++ 2014 Standard

int f(std::vector<std::string> s) {
  int len = s.size();
  return len;
}
std::string fUpper(std::string s) { 
    std::for_each(s.begin(), s.end(), [](char & c){
        c = ::toupper(c);
    });
    return s;
}

std::string fLower(std::string s) { 
    std::for_each(s.begin(), s.end(), [](char & c){
        c = ::tolower(c);
    });
    return s;
}

void printString(std::string s) {
    printf("%s ", s.c_str());
}

void printStrings(std::vector<std::string> cities){
    std::for_each(cities.begin(), cities.end(), printString);
    printf("\n");
}
void f1() {
    std::vector<std::string> cities = {"Athens", "Roma"};
    std::for_each(cities.begin(), cities.end(), [](std::string & str){
        str = fUpper(str);
    });
    printStrings(cities);

    std::for_each(cities.begin(), cities.end(), [](std::string & str){
        str = fLower(str);
    });
    printStrings(cities);
}

int main() {
    std::vector<std::string> cities = {"Athens",  "Roma", "London",
                                     "Beijing", "Kiev", "Riga"};
    f1();
    printf("%d\n", f(cities));
}