int longestSubarray(int* nums, int numsSize) {
    bool flag = false;
    int one = 0;
    int two = 0;
    int answer = 0;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) {
            if (one + two > answer) {
                answer = one + two;
            }
            one = two;
            two = 0;
            flag = true;
        } else {
            two++;
        }
    }
    if (one + two > answer) {
        answer = one + two;
    }
    
    if (flag == false) {
        answer--;
    }
    
    return answer;
}