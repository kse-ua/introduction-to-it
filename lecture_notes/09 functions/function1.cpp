#include <stdio.h>

int add1(int first_num, int sec_num){
    return first_num + sec_num;
}

int add2(int n1, int n2){
    int res;
    res = n1 + n2;
    return res;
}

int main(){
    int res = add1(10, 20);
    printf("%d\n", res);
    res = add2(10, 20);
    printf("%d\n", res);
}
