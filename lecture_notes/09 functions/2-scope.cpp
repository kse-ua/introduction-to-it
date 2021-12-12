#include <iostream>
using namespace std;

string cities[] = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};
int len = sizeof(cities) / sizeof(string);

void print_cities(string s[], int len) {
    cout << "cities: [ ";
    for(int idx = 0; idx < len; idx++) {
        cout << s[idx] << " ";
    }
    cout << "]\n";
}

void print_len() {
    cout << "[ ";
    for(int i = 0; i < len; i++) {
        cout << cities[i].size() << " ";
    }
    cout << "]\n";
}

string to_upper(string s) {
    for(int i = 0; i < s.size(); i++){
        s[i] = toupper(s[i]);
    }
    return s;
}

string to_lower(string s) {
    for(int i = 0; i < s.size(); i++){
        s[i] = tolower(s[i]);
    }
    return s;
}

void f1() {
    string cities[] = {"Athens", "Roma"};
    int len = sizeof(cities)/sizeof(string);
    string upper[len];
    for (int idx = 0; idx < len; idx++) {
        upper[idx] = to_upper(cities[idx]);
    }
    print_cities(cities, len);
    print_cities(upper, len);
    string lower[len];
    for (int idx = 0; idx < len; idx++) {
        lower[idx] = to_lower(cities[idx]); 
    }
    print_cities(cities, len);
    print_cities(lower, len);
    {
        string cities[] = {"London", "Beijing", "Kiev"};
        len = sizeof(cities)/sizeof(string);
        string upper[len];
        for(int idx = 0; idx < len; idx++) {
            upper[idx] = to_upper(cities[idx]);
        }
        print_cities(cities, len);
        print_cities(upper, len);
    }
}

int main() {
    f1();
    print_cities(cities, len);
    print_len();
    return 0;
}
