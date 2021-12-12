#include <iostream>
using namespace std;
#include <stdarg.h>

// this doesn't work at all
//void catchRest(int length, ...) {
//string result[length];
//    for(int i = 0; i < 4; i++) {
//        cout << result[length] << " ";
//    }
//  cout << endl;
//}



int main() {
    // catchRest(1, 2, 3);
    // trying to pretend it works like that
    cout << "Enter a number: ";
    int number;
    cin >> number;
    cout << "The type of " << number << " is int \n"; 
    cout << "Enter a word: ";
    string word;
    cin >> word;
    cout << "The type of " << word << " is string";
    return 0;
}


