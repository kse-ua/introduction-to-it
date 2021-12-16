#include <iostream>
using namespace std;

int PointsShift(const int arr[]) {

    int test[4][2] =
            {
                    {0, 0},
                    { 10, 10},
                    {20, 20},
                    {30, 30}
            };

    int polygon[4][2];

    for (auto & i : test) {
        for (int j = 0; j < 2; ++j) {
            if (j == 0) {
                cout << "x, y = " << i[j];
            } if (j == 1) {
                cout << ", " << i[j] << "\n";
            }
        }
    }
    
    cout << "\n" << "Adding new values from parameter..." << endl << "\n";
    for (auto & i : test) {
        for (int j = 0; j < 2; ++j) {
            if (j == 0) {
                cout << "x, y = " << i[j];
            } if (j == 1) {
                i[j] += arr[j];
                cout << ", " << i[j] << "\n";
            }
        }
    }
    return 0;
}

int main() {
    int arr[] = {10, -5};
    PointsShift(arr);
    return 0;
}
