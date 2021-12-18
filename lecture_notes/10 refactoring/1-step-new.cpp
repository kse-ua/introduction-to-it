# include <iostream>
# include <string>
# include <map>
# include "nlohmann.h"
# include <typeinfo>

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

int addingValues(const int arr[]) {
    map<string, int> polyline[] = {
            {
                    {"x", 0},
                    {"y", 0},
            },

            {
                    {"x", 10},
                    {"y", 10},
            },

            {
                    {"x", 20},
                    {"y", 20},
            },

            {
                    {"x", 30},
                    {"y", 30},
            }
    };

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

    Parse(polylines, 4);

    for (auto & poly : polylines) {
        for (const auto &p : poly.dict) {
            cout << "m[" << p.first << "] = " << p.second << '\n';
        }
    }
    cout << "\n" << "Adding new values ..." << endl << "\n";
    for (auto & poly : polylines) {
        for (const auto &p: poly.dict) {
            if( p.first == "x") {
                int a = p.second + arr[0];
                cout << "m[" << a << "] = " << a << '\n';
            }
            else if ( p.first == "y") {
                int a = p.second + arr[1];
                cout << "m[" << a << "] = " << a << '\n';
            }

        }
    }

    return 0;

}

int main() {
    int arr[] = {10, -5};
    addingValues(arr);
}
