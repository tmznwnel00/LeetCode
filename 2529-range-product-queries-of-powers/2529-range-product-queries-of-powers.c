/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>
#define MOD 1000000007

int* productQueries(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int powers[32];
    
    int index = 0;
    long long temp = 1;
    int temp_n = n; 
    
    while (temp_n) {
        if (temp_n == 1){
            powers[index++] = 1;
            break; 
        }
        if (temp > temp_n){
            temp /= 2;
            temp_n -= (int)temp;
            powers[index++] = (int)temp;
            temp = 1;
        } else {
            temp *= 2;
        }
    }

    for (int i = 0; i < index / 2; i++){
        int tmp = powers[i];
        powers[i] = powers[index - 1 - i];
        powers[index - 1 - i] = tmp;
    }

    int* answer = (int*)malloc(sizeof(int) * queriesSize);
    *returnSize = queriesSize;
    
    for (int i = 0; i < queriesSize; i++){
        int x = queries[i][0];
        int y = queries[i][1];

        long long prod = 1;
        for (int j = x; j <= y; j++) {
            prod = (prod * powers[j]) % MOD;
        }
        answer[i] = (int)prod;
    }

    return answer;
}