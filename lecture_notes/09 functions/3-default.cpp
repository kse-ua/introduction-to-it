#include <stdio.h>

int max(int a = 0, int b = 0)
{
    return (a > b ? a : b);
}

int main()
{
    printf("[ %d, %d, %d ] ", max(10, 20), max(10), max(-20));
}