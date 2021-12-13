#include <iostream>
using namespace std;

// Function that calculates len of each element in array
void mainOutput() {
    string cities[] = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};

    for (int i = 0; i < 5; i++) {
      cout << cities[i].size() << " ";
    }

}

int main() {
    string FirstCities[] = {"Athens", "Roma"};

    for (auto & citie : FirstCities) {
        transform(citie.begin(), citie.end(), citie.begin(), ::toupper);
        cout << citie << endl;
    }

    cout << endl;

    for (auto & citie : FirstCities) {
        transform(citie.begin(), citie.end(), citie.begin(), ::tolower);
        cout << citie << endl;
    }

    cout << endl;

    string ThirdCities[] = {"London", "Beijing", "Kiev"};

    for (auto & citie : ThirdCities) {
        transform(citie.begin(), citie.end(), citie.begin(), ::toupper);
        cout << citie << endl;
    }

    cout << endl;
    mainOutput();

    return 0;
}
