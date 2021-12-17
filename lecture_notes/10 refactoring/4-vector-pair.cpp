#include <iostream>
#include <vector>
#include <string>

// Tried to use vector instead of map;
std::vector<std::pair<std::string, int>> offset = { {"x", 10}, {"y", -5}, };
std::vector<std::pair<std::string, int>> points = { {"x", 0},  {"y", 0}, 
                                                    {"x", 10}, {"y", 10}, 
                                                    {"x", 20}, {"y", 20}, 
                                                    {"x", 30}, {"y", 30}, 
                                                  };


int main() {

    int pointsLength = size(points);
    for (int i = 0; i < pointsLength; i += 2) {

        points[i].second += offset[0].second;
        points[i + 1].second += offset[1].second;

        std::cout << points[i].first << " = " << points[i].second <<
        ", " << points[i + 1].first << " = " << points[i + 1].second << std::endl;
    }

    return 0;
}
