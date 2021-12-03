using namespace std;
#include <iostream>

int* concat_array(int array1[], int array2[], int firstLength, int secondLength){
    int length = firstLength + secondLength;
    int new_array[length];

    for(int i = 0; i < firstLength; i++){
        new_array[i] = array1[i];
    }
    for(int i = 0; i < secondLength; i++){
        new_array[i + firstLength] = array2[i];
    }
    for(int i = 0; i < length; i++){
        cout << new_array[i] << endl;
    }
}

int main() {
    int schoolAges[] = {10, 12, 15, 15};
    int studentAges[] = {17, 18, 18, 19, 20};
    int firstLength = sizeof(schoolAges) / sizeof(int);
    int secondLength = sizeof(studentAges) / sizeof(int);
    concat_array(schoolAges, studentAges, firstLength, secondLength);
}
