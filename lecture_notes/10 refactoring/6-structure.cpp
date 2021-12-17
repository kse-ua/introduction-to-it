#include <iostream>
#include <vector>
using namespace std;

// Vector offset;
vector<pair<string, int>> offset = { {"x", 10}, {"y", -5}, };

// Tried structure instead of vector;
struct Point {

    int x, y;

    void printDetails () {

        cout << "x = " << x << 
        ", y = " << y << endl;

    }

};

int main() {

    // Create an array of structures;
    struct Point arr[4];

    arr[0] = {0, 0};
    arr[1] = {10, 10};
    arr[2] = {20, 20};
    arr[3] = {30, 30};

    int arrSize = size(arr);
    for (int i = 0; i < arrSize; i++) {

        arr[i].x += offset[0].second;
        arr[i].y += offset[1].second;
    }

    for (int i = 0; i < arrSize; i++) {

        arr[i].printDetails();
    }

    return 0;
}
