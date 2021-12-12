#include <stdio.h>

int max(int a = 0, int b = 0) {
    if(a > b) {
        return a;
    }
    else {
        return b;
    }
}

int main() {
    printf("[%d, %d, %d]\n", max(10, 20), max(10), max(-20));
}