#include <iostream>
#include <vector>
#include <stdint.h>

/*
assign() – It assigns new value to the vector elements by replacing old ones
push_back() – It push the elements into a vector from the back
pop_back() – It is used to pop or remove elements from a vector from the back.
insert() – It inserts new elements before the element at the specified position
erase() – It is used to remove elements from a container from the specified position or range.
swap() – It is used to swap the contents of one vector with another vector of same type. Sizes may differ.
clear() – It is used to remove all the elements of the vector container
emplace() – It extends the container by inserting new element at position
emplace_back() – It is used to insert a new element into the vector container, the new element is added to the end of the vector
*/

int main() {
    std::vector<int> ages = {10, 12, 15, 15, 17, 18, 18, 19, 20};
    int first = ages.front();
    int last = ages.back();
    printf("result: %d\n", first);
    printf("result: %d\n", last);

    ages.pop_back();
    ages.push_back(22);

    for (int i = 0; i < ages.size(); i++)
        std::cout << ages[i] << " ";
}
