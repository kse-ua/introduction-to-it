#include <stdio.h>
#include <string>
#include <cctype> 
#include <algorithm>
#include <ctype.h> 
#include <iostream>

using namespace std;
using std::toupper;
using std::tolower;

string cities[] = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};
int cities_lenght = sizeof(cities) / sizeof(string);

int * f(string array[], int lenght) {
    int* lenghtOfStrings = new int[lenght];
    for (int i = 0; i < lenght ; i++) {
        lenghtOfStrings[i] = array[i].size();
  }
  return lenghtOfStrings;
}

string upper(string element) {
    for (int i = 0; i < element.size() ; i++) {
        element[i] = toupper(element[i]);
    }
    return element;
}

string lower(string element) {
    for (int i = 0; i < element.size() ; i++) {
        element[i] = tolower(element[i]);
    }
    return element;
}

void f1() {
    string cities[] = {"Athens", "Roma"};
    int cities_lenght = sizeof(cities) / sizeof(string);

    for (int i = 0; i < cities_lenght ; i++) {
        cities[i] = upper(cities[i]);
        cout << cities[i] << std::endl;
    }

    for (int i = 0; i < cities_lenght ; i++) {
         cities[i] = lower(cities[i]);
         cout << cities[i] << std::endl;
    }
    
    {
        string cities[] = {"London", "Beijing", "Kiev"};
        int lenght = sizeof(cities) / sizeof(string);
        int* lenght_cities = f(cities, lenght);
        for (int i = 0; i < lenght; i++) {
            cout << lenght_cities[i] << std::endl;
    }
    } 
}


int main()
{
    f1();
    // console.dir(cities.map(f))
    int* map = f(cities, cities_lenght);
    for (int i = 0; i < cities_lenght; i++) {
         cout << map[i] << std::endl;
    }
    return 0;
};
