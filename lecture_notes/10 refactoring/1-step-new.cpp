# include <iostream>
# include <string>
# include <map>

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
        if (polylines->type == Dictionary) {
            //
        }
        else if (polylines->type == String) {
            //
        }
    }
}

int main() {
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

    int a = polyline[1]["x"];
    cout << a << endl;
    return 0;

}
