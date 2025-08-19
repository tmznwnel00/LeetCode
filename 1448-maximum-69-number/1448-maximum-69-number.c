#include<stdio.h>
#include<string.h>

int maximum69Number (int num) {
    
    char answer[5];
    char temp[5];
    sprintf(temp, "%d", num);
    bool flag = true;
    for (int i = 0; i < strlen(temp); ++i) {
        if (temp[i] == '6' && flag) {
            answer[i] = '9';
            flag = false;
        } else {
            answer[i] = temp[i];
        }
    }
    int answer_int = atoi(answer);

    return answer_int;


}