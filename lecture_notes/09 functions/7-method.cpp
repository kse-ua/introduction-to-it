#include <iostream>
using namespace std;
class Counter {
    public:
        int value = 0;

        void inc(int x) {
            value += x;
        }
};

int main() {
    Counter counter;

    counter.inc(10);
    cout << "{ counter: { value: " << counter.value << ", inc: [Function: inc] } }" << endl;
    // cout << counter.value << endl;

    counter.inc(20);
    cout << "{ counter: { value: " << counter.value << ", inc: [Function: inc] } }" << endl;

    return 0;

}
