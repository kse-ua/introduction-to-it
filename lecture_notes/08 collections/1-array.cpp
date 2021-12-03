#include <stdio.h>
#include <vector>

int main() {
    std::vector <int> ages = { 10, 12, 15, 15, 17, 18, 18, 19, 20, 45 };

    ages.push_back(34);

    int first = ages[0];
    int length;
    length = ages.size();
    int last = ages[length - 1];

    printf("first: %d\n", first);
    printf("last: %d\n", last);
}


