#include <iostream>
#include <map>
#include <variant>
#include <vector>

/*
I've implemented a simple custom recursive-descent LL(1) json parser since cpp has no builtin json parser.
It needs further improvements but it was a 2-night work :)
*/
#include "json.h"
#include "parser.h"

using namespace std;
using namespace json;

class Point {
private:
    int x;
    int y;
public:
    Point(int x1, int y1) {
        x = x1;
        y = y1;
    }

    [[nodiscard]] int get_x() const {
        return x;
    }

    [[nodiscard]] int get_y() const {
        return y;
    }

    static Point parse(variant<map<string, int>, string> object) {
        int x1, y1;
        if (holds_alternative<string>(object)) {
            pjson parsed = parser(get<string>(object)).parse();
            x1 = parsed->get<int>("x");
            y1 = parsed->get<int>("y");
        } else {
            auto point = get<map<string, int>>(object);
            x1 = point["x"];
            y1 = point["y"];
        }

        return {x1, y1};
    }

    [[nodiscard]] Point move(map<string, int> offset) const {
        int x1 = x + offset["dx"];
        int y1 = y + offset["dy"];

        return {x1, y1};
    }

};


void print_points(const vector<Point>& points) {
    cout << "[ " << endl;
    for (const auto& p : points) {
        cout << "\t{ x: " << p.get_x() << ", y: " << p.get_y() << " }" << endl;
    }
    cout << "]" << endl;
}

int main() {
    map<string, int> offset{{"dx", 10},
                            {"dy", -5}};
    variant<map<string, int>, string> json(R"({ "x": 20, "y": 20 })");
    vector<variant<map<string, int>, string>> polyline{
            map<string, int>({{"x", 0},
                              {"y", 0}}),
            map<string, int>({{"x", 10},
                              {"y", 10}}),
            json,
            map<string, int>({{"x", 30},
                              {"y", 30}}),
    };
    vector<Point> points;
    points.reserve(polyline.size());
    for (const auto &point: polyline) {
        points.push_back(Point::parse(point));
    }
    vector<Point> path;
    path.reserve(points.size());
    for (const auto &point: points) {
        path.push_back(point.move(offset));
    }

    print_points(path);

    return 0;
}
