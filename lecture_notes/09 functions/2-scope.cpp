using namespace std;
#include <iostream>

string cities[] = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};
int length = sizeof(cities)/sizeof(string);

string toUpperCase(string s){
    for(int i = 0; i < s.length(); i++){
        s[i] = toupper(s[i]);
    }
    return s;
}

string toLowerCase(string s){
    for(int i = 0; i < s.length(); i++){
        s[i] = tolower(s[i]);
    }
    return s;
}

void printArray(string s[], int length){
    cout << "[ ";
    for(int i = 0; i < length; i++){
        cout << s[i] << ' ';
    }
    cout << "] " << endl;
}

void f1(){
    string cities[] = {"Athens", "Roma"};
    int length = sizeof(cities)/sizeof(string);
    string upperCities[length];
    string lowerCities[length];
    for(int i = 0; i < length; i++){
        upperCities[i] = toUpperCase(cities[i]);
    }
    for(int i = 0; i < length; i++){
        lowerCities[i] = toLowerCase(cities[i]);
    }

    printArray(cities, length);
    printArray(upperCities, length);

    printArray(cities, length);
    printArray(lowerCities, length);

    {
        string cities[] = {"London", "Beijing", "Kiev"};
        length = sizeof(cities)/sizeof(string);
        string upperCities[length];
        for(int i = 0; i < length; i++){
            upperCities[i] = toUpperCase(cities[i]);
        }
        printArray(cities, length);
        printArray(upperCities, length);
    }
}

int main() {
    f1();
    printArray(cities, length);
    int lengthArr[length];

    cout << "[ ";
    for(int i = 0; i < length; i++){
        cout << cities[i].length() << " ";
    }
    cout << "]" << endl;
}

