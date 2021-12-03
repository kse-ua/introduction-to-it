#include <stdio.h>

void getFirstAndLast (int ages[],int len, int* first, int* last)
{
    int a = ages[0];
    int b = ages[len - 1];
    *first = a;
    *last = b;
  
}

int main ()
{
    
    int ages[] = { 10, 12, 15, 15, 17, 18, 18, 19, 20 };
    int len = sizeof (ages) / sizeof(int);
    int first, last;
    
    getFirstAndLast (ages, len, &first, &last);

    printf ("{first: %d}\n{last: %d}\n", first, last);
}
