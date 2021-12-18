# include <iostream>
# include <string>
# include <map>
# include "nlohmann.h"

using json = nlohmann::json;
using namespace std;

enum Type {
    Dictionary,
    String
};

struct PolylineEntry {
    map<string, int> dict;
    string str;
    Type type;
};

// Converting string type to map, using json
void Parse(PolylineEntry polylines[], int size) {
    for (int i = 0; i < size; i++) {
        if (polylines[i].type == String) {
            auto jsonParsed = json::parse(polylines[i].str);
            polylines[i].dict = {
                    {"x", jsonParsed["x"]},
                    {"y", jsonParsed["y"]}
            };
            polylines[i].type = Dictionary;
        }
    }
}

// Creating global var.
PolylineEntry entry0 = {
        {
                {"x", 0},
                {"y", 0},
        },
        "",
        Dictionary
};

PolylineEntry entry1 = {
        {
                {"x", 10},
                {"y", 10},
        },
        "",
        Dictionary
};

PolylineEntry entry2 = {
        {},
        R"({"x": 20, "y": 20})",
        String
};

PolylineEntry entry3 = {
        {
                {"x", 30},
                {"y", 30},
        },
        "",
        Dictionary
};

PolylineEntry polylines[] = {
        entry0,
        entry1,
        entry2,
        entry3,
};

int addingValues(std::map<string, int> &offset) {
    Parse(polylines, 4);

    // Outputting starting points
    for (auto & poly : polylines) {
        for (const auto &p : poly.dict) {
            cout << "m[" << p.first << "] = " << p.second << '\n';
        }
    }

    cout << "\n" << "Adding new values ..." << endl << "\n";

    for (auto & poly : polylines) {
        for (const auto &p: poly.dict ) {
            if( p.first == "x") {
                int a = p.second + offset["x"];
                cout << "m[" << p.first << "] = " << a << '\n';
            }
            else if ( p.first == "y") {
                int a = p.second + offset["y"];
                cout << "m[" << p.first << "] = " << a << '\n';
            }

        }
    }
    return 0;
}


int main() {
    map<string, int> offset{{"x", 10}, {"y", -5}};
    addingValues(offset);
}

// Thanks to Chak Franklin, for explaining out how to properly convert string to map format:)
