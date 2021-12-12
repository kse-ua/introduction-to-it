#include <iostream>

int max(int a = 0, int b = 0) {
    return a > b ? a : b;
}

int main() {
    int a = max(10, 20);
    printf("%d, ", a);
    int b = max(10);
    printf("%d, ", b);
    int c = max(-20);
    printf("%d", c);
    return 0;
}
