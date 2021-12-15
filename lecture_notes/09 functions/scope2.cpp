using namespace std;

#include <iostream>

string cities[] = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};
int length = sizeof(cities) / sizeof(string);

string UpperCase(string world) {
    for (int i = 0; i < world.length(); i++) {
        world[i] = toupper(world[i]);
    }
    return world;
}

string LowerCase(string world) {
    for (int i = 0; i < world.length(); i++) {
        world[i] = tolower(world[i]);
    }
    return world;
}

void printArray(string world[], int length) {
    cout << "[ ";
    for (int i = 0; i < length; i++) {
        cout << world[i] << ' ';
    }
    cout << "] " << endl;
}

int main() {
    printArray(cities, length);
    cout << UpperCase(cities[0]) << ' ' << UpperCase(cities[1]) << endl;
    cout << LowerCase(cities[0]) << ' ' << LowerCase(cities[1]) << endl;
    cout << UpperCase(cities[2]) << ' ' << UpperCase(cities[3]) << ' ' << UpperCase(cities[4]) << endl;
    cout << cities[0].length() << ' ' << cities[1].length() << ' ' << cities[2].length() << ' ' <<
         cities[3].length() << ' ' << cities[4].length() << ' ' << cities[5].length() << endl;
    return 0;
}
