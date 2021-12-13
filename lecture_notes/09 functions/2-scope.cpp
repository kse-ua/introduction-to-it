#include <iostream>
using namespace std;

// Function that calculates len of each element in array
void LengthElements() {
    string cities[] = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};

    for (int i = 0; i < 5; i++) { cout << cities[i].size() << " ";  }

}

// Functions were created function to improve the readability of code 

void ToUpperFirst() {
    string FirstCities[] = {"Athens", "Roma"};

    for (auto & city : FirstCities) {
        transform(city.begin(), city.end(), city.begin(), ::toupper);
        cout << city << endl;
    }

    cout << endl;

}

void ToLowerFirst() {
    string FirstCities[] = {"Athens", "Roma"};

    for (auto & city : FirstCities) {
        transform(city.begin(), city.end(), city.begin(), ::tolower);
        cout << city << endl;
    }

    cout << endl;

}

void ToUpperSecond() {
    string ThirdCities[] = {"London", "Beijing", "Kiev"};

    for (auto & city : ThirdCities) {
        transform(city.begin(), city.end(), city.begin(), ::toupper);
        cout << city << endl;
    }

    cout << endl;

}

int main() {
    ToUpperFirst();
    ToLowerFirst();
    ToUpperSecond();
    LengthElements();

    return 0;
}
