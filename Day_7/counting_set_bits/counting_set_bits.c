#include<stdio.h>

int count_set_bits(int num){
    int count = 0;
    while (num){
        count += num && 1;
        num >>= 1;
    }

    return count;
}

void main(){
    int n = 5;
    int res = count_set_bits(n);
    printf("%d", res);
}