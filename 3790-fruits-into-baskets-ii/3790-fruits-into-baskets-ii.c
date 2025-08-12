int numOfUnplacedFruits(int* fruits, int fruitsSize, int* baskets, int basketsSize) {
    int answer = 0;

    for (int i = 0; i < fruitsSize; i++){
        int fruit = fruits[i];
        int index = 0;
        int flag = 0;

        for (int j = 0; j < basketsSize; j++) {
            if (baskets[j] >= fruit) {
                baskets[j] = -1;
                flag = 1;
                break;
            }
        }

        if (!flag) {
            answer ++;
        }
    }
    return answer;
}