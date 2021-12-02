#include <stdio.h>

int main()
{
    int ages[] = {10, 12, 15, 15, 17, 18, 18, 19, 20};

    int first = ages[0];
    int length = sizeof(ages) / sizeof(ages[0]);
    int last = ages[length - 1];

    printf("first: %d\n", first);
    printf("last: %d\n", last);

    // Push to the end
    int push_ages[length + 1];
    for (int i = 0; i < length + 1; i++){
        push_ages[i] = ages[i]; 
    }
    push_ages[length] = -1003; 
    printf("last: %d\n", push_ages[length]);

    // Pop the last one
    int pop_ages[length - 1];
    for (int i = 0; i < length - 1; i++){
        pop_ages[i] = ages[i];
    }
    printf("last: %d\n", pop_ages[length - 2]);

    // Add to the top
    int add_ages[length + 1];
    for (int i = 0; i < length + 1; i++){
        add_ages[i+1] = ages[i];
    }
    add_ages[0] = -832;
    printf("second: %d\n", add_ages[1]); 

    // Remove the first one
    int shift_ages[length - 1];
    for (int i = 0; i < length - 1; i++){
        add_ages[i] = ages[i+1];
    }
    printf("first: %d\n", add_ages[0]);
}
