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

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 2; ++j) {
            cout << " test[" << i << "][" << j << "] = " << test[i][j] << endl;
        }
        if (int j = 1) {
            cout << endl;
        }
    }

    cout << "\n" << "Adding new values from parameter..." << endl << "\n";

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 2; ++j) {
            test[i][j] += arr[j];
            cout << "test[" << i << "][" << j << "] = " << test[i][j] << endl;
        }
        if (int j = 1) {
            cout << endl;

        }
    }

    return 0;
}


int main() {
    int arr[] = {10, -5};

    PointsShift(arr);
    return 0;
}

