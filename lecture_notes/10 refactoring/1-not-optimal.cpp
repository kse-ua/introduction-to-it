#include <iostream>
#include <stdio.h>
#include <string>
#include <map>

// Create arguments;
std::map<std::string, int> offset { {"x", 10}, {"y", -5} };
std::map<std::string, int> points { {"x1", 0},  {"y1", 0},
                                    {"x2", 10}, {"y2", 10},
                                    {"x3", 20}, {"y3", 20},
                                    {"x4", 30}, {"y4", 30},
                                  };


int shift(std::map<std::string, int> offset, std::map<std::string, int> X) {

    points["x1"] += offset["x"];
    points["y1"] += offset["y"];

    points["x2"] += offset["x"];
    points["y2"] += offset["y"];

    points["x3"] += offset["x"];
    points["y3"] += offset["y"];

    points["x4"] += offset["x"];
    points["y4"] += offset["y"];

    return 0;
};

int main() {

    shift(offset, points);

    // auto assign a type to item;
    for (auto item : points) {
        
        std::cout << item.first << ": " << item.second << std::endl;
    }

    return 0;
}
