
#include <iostream> // input and output info from out code
using namespace std;  // Declaring on a global level

void mainOutput() {
    string cities[] = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};

    for (int i = 0; i < 5; i++) { cout << cities[i].size() << " ";  }

}

int main() {
    mainOutput();

    cout << endl;
    
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

    return 0;
}
