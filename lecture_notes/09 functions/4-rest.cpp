#include <iostream>
using namespace std;

// I know that I'm passing an array to the parameters, but hey, I've spent 3 hours to implement the same functionality as in 4-rest.py, but cannot handle this :(
void print_args(int args[], int length) {

    for (int index = 0; index < length; index++) {
        cout << args[index] << " ";
    }
}

int main() {

    int args[] = { 1, 2, 3, 5, 100, 3232 };
    int length = sizeof(args) / sizeof(int);

    cout << "( ";
    print_args(args, length);
    cout << ")" << endl;

    return 0;
}
