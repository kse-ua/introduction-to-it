#include <cstdio>
#include <cstring>

using namespace std;

int* concat(int* array1, int length_array1, int* array2, int length_array2) {
    int* result = new int[length_array1 + length_array2];

    memcpy(result, array1, length_array1 * sizeof(int));
    memcpy(result + length_array1, array2, length_array2 * sizeof(int));

    return result;
}


int main() {
    int school_ages[] = { 10, 12, 15, 15 };
    int student_ages[] = { 17, 18, 18, 19, 20 };
    int school_length = sizeof(school_ages) / sizeof(int);
    int student_length = sizeof(student_ages) / sizeof(int);
    int length = school_length + student_length;

    int* ages = concat(school_ages, school_length, student_ages, student_length);

    for (int i = 0; i < length; i++) {
        printf("ages[%d]: %d\n", i, ages[i]);
    }

    return 0;
}
