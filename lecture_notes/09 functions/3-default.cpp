#include <stdio.h>
#include <iostream>

int max(int a = 0, int b = 0) {
    int result = a > b ? a : b;
    return result;
};

int main() {
    int result[3] = {
        max(10, 20),
        max(10),
        max(-20),
    };
    int sizeResult = sizeof(result) / sizeof(int);
    for (int i = 0; i < sizeResult; i++) {
        printf("%d\n", result[i]);
    }
}
