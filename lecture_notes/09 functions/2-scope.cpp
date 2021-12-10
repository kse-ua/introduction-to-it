#include <cctype>
#include <iostream>
#include <cstring>
using namespace std;

// Returns word length;
int length(std::string s) {
     int length = s.size();
     return length;
};

// Converts to uppercase;
int upperCase(std::string s) {
    const char *sChar = s.c_str();
    char ch;
    std::string result;
    for (int i = 0; i < strlen(sChar); i++) {
        ch = toupper(sChar[i]);
        result += ch;
    }
    std::cout << result << std::endl;
    return 0;
};

// Converts to lowercase;
int lowerCase(std::string s) {
    const char *sChar = s.c_str();
    char ch;
    std::string result;
    for (int i = 0; i < strlen(sChar); i++) {
        ch = tolower(sChar[i]);
        result += ch;
    }
    std::cout << result << std::endl;
    return 0;
};

// Blocks of code, called upper/lower functions;
int f1() {
    std::string cities[] = {"Athens", "Rome"};
    int sizeCities = sizeof(cities) / sizeof(std::string);
    for (int i = 0; i < sizeCities; i++) {
        upperCase(cities[i]);
        lowerCase(cities[i]);
    }

    {
        std::string cities[] = {"London", "Beijing", "Kiev"};
        int sizeCities = sizeof(cities) / sizeof(std::string);
        for (int i = 0; i < sizeCities; i++) {
            upperCase(cities[i]);
        }
    }
    return 0;
};


int main() {
    std::string cities[] = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};
    int sizeCities = sizeof(cities) / sizeof(std::string);
    for (int i = 0; i < sizeCities; i++) {
        int size = length(cities[i]);
        std::cout << cities[i] << " word length is " << size << std::endl;
    }
    f1();
    return 0;
}
