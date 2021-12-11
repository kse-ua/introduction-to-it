#include <iostream>
using namespace std;

string cities[] = { "Athens", "Roma", "London", "Beijing", "Kiev", "Riga" };
int length = sizeof(cities) / sizeof(string);

void print_cities(string cities[], int length) {

    cout << "[ ";
    for (int index = 0; index < length; index++) {
        cout << cities[index] << ' ';
    }
    cout << "]" << endl;
}

void print_cities_length() {

    print_cities(cities, length);
    cout << "[ ";
    for (int a = 0; a < length; a++) {
        cout << cities[a].length() << " ";
    }
    cout << "]" << endl;
}

string to_upper(string city) {

    for (int letter = 0; letter < city.length(); letter++) {
        city[letter] = toupper(city[letter]);
    }

    return city;
}

string to_lower(string city) {

    for (int letter = 0; letter < city.length(); letter++) {
        city[letter] = tolower(city[letter]);
    }

    return city;
}

void transform() {

    string cities[] = { "Athens", "Roma" };
    int length = sizeof(cities) / sizeof(string);

    string upper_cities[length];
    for (int index = 0; index < length; index++) {
        upper_cities[index] = to_upper(cities[index]);
    }
    print_cities(cities, length);
    print_cities(upper_cities, length);

    string lower_cities[length];
    for (int index = 0; index < length; index++) {
        lower_cities[index] = to_lower(cities[index]);
    }
    print_cities(cities, length);
    print_cities(lower_cities, length);

    {
        string cities[] = { "London", "Beijing", "Kiev" };
        length = sizeof(cities) / sizeof(string);

        string upper_cities[length];
        for (int index = 0; index < length; index++) {
            upper_cities[index] = to_upper(cities[index]);
        }
        print_cities(cities, length);
        print_cities(upper_cities, length);
    }
}

int main() {

    transform();
    print_cities_length();

    return 0;
}
