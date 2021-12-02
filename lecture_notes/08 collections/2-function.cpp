#include <stdio.h>

int get_first(int array[], int length)
{
    if (length > 0)
    {
        return array[0];
    }
    return -1;
}

int get_last(int array[], int length)
{
    if (length > 0)
    {
        return array[length - 1];
    }
    return -1;
}

int main()
{
    int ages[] = {10, 12, 15, 15, 17, 18, 18, 19, 20};
    int length = sizeof(ages) / sizeof(ages[0]);

    int first = get_first(ages, length);
    int last = get_last(ages, length);
    printf("first: %d\n", first);
    printf("last: %d\n", last);
}
