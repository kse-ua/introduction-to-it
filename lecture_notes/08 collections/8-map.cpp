#include <iostream>
#include <map>
#include <string>

using namespace std;


void print_map(const map<string, int>& m) {
    cout << "Map: { ";
    for (const auto& kv : m) {
        cout << kv.first << " = " << kv.second << " ";
    }
    cout << "}" << endl;
}

int main() {
    map<string, int> ages;

    ages.insert({"Vasia Pupkin", 19});
    ages.insert({"Marcus Aurelius", 1860});
    print_map(ages);

    ages["Vasia Pupkin"] = 20;
    print_map(ages);

    ages.erase("Vasia Pupkin");

    cout << boolalpha;
    cout << "Marcus Aurelius: " << (ages.find("Marcus Aurelius") != ages.end()) << endl;
    cout << "Vasia Pupkin: " << (ages.find("Vasia Pupkin") != ages.end()) << endl;

    ages.clear();
    print_map(ages);

    return 0;
}