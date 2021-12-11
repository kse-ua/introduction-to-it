#include <stdio.h>

int max(int a = 0, int b = 0) {
    if (a > b) return a;
    return b;
}

int main () {
    printf("10,20: %d\n", max(10, 20));
    printf("10: %d\n", max(10));
    printf("-20: %d\n", max(-20));
}
