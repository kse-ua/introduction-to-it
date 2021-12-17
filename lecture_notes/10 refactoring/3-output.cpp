#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
#include <set>

// Create (x, value), (y, value) pairs;
std::map<std::string, int> offset { {"x", 10}, {"y", -5} };
std::map<std::string, int> points { {"x1", 0},  {"y1", 0},
                                    {"x2", 10}, {"y2", 10},
                                    {"x3", 20}, {"y3", 20},
                                    {"x4", 30}, {"y4", 30},
                                  };

int main() {

    // Tried not to change original maps;
    std::map <std::string, int> output;

    // Contains keys;
    std::set<std::string> keysX { "x1", "x2", "x3", "x4" };

    // auto assign a type to item, & is a reference to <str::string, int>;
    for (auto& item : points) {

        if (keysX.count(item.first) != 0) {
            output[item.first] = item.second + offset["x"];
        }

        else {
            output[item.first] = item.second + offset["y"];
        }
    }

    // Print output
    for (auto item : output) {

        std::cout << item.first << ": " << item.second << std::endl;
    }

    return 0;
}
