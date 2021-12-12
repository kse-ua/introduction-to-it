#include <iostream>
using namespace std;

string cities[] = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};
int length = sizeof(cities)/sizeof(string);

string upperCase(string element) {
    for(int letter = 0; letter < element.length(); letter++) {
        element[letter] = toupper(element[letter]);
    }
    return element;
}

string lowerCase(string element) {
    for(int letter = 0; letter < element.length(); letter++) {
        element[letter] = tolower(element[letter]);
    }
    return element;
}


void printingCities(string cities[], int length) {
    cout << "[ ";
    for(int index = 0; index < length; index++) {
        cout << cities[index] << ", ";
    }
    cout << "]" << endl;
}


void printingLengthOfCities() {
    printingCities(cities, length);
    cout << "[ ";
    for (int index = 0; index < length; index++) {
        cout << cities[index].length() << ", ";
    }
    cout << "]" << endl;
}


void function() {
    string cities[] = {"Athens", "Roma"};
    int length = sizeof(cities) / sizeof(string);
    
    string bigLetterCities[length];
    for (int i = 0; i < length; i++) {
        bigLetterCities[i] = upperCase(cities[i]);
    }
    printingCities(cities, length);
    printingCities(bigLetterCities, length);
    
    
    string smallLetterCities[length];
    for (int i = 0; i < length; i++) {
        smallLetterCities[i] = lowerCase(cities[i]);
    }
    printingCities(cities, length);
    printingCities(smallLetterCities, length);
    
    {
        string anotherCities[] = {"London", "Beijing", "Kiev"};
        length = sizeof(anotherCities)/sizeof(string);
        
        string newCities[length];
        for(int i = 0; i < length; i++) {
            newCities[i] = upperCase(anotherCities[i]);
        }
        printingCities(anotherCities, length);
        printingCities(newCities, length);
    }
}


int main() {
    function();
    printingLengthOfCities();
}
