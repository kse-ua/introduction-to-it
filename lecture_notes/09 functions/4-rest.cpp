#include <iostream>
#include <cstdarg>
using namespace std;

// Variable number of elements;
int* catchRest(int num, ... ) {
    int* result = new int[num];

    va_list valist;
    va_start(valist, num);
    for (int i = 0; i < num; i++) {
        result[i] = va_arg(valist, int);
    }
    va_end(valist);
    return result;
};

// Returns arguments, if object returns string
int f2(int num, ... ) {
    std::string result[num]; 

    va_list valist;
    va_start(valist, num);
    for (int i = 0; i < num; i++) {
        result[i] = std::to_string(va_arg(valist, int));
        std::cout << result[i] << std::endl;
    }

    va_end(valist);
    return 0;
};


int main() {
    int* result = catchRest(3, 1, 2, 3);
    for (int i = 0; i < 3; i++) {
        printf("%d\n", result[i]);
    }
    f2(3, 13, 11, 1975);
    return 0;
}
