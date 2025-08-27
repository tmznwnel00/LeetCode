int compare_desc(const void* a, const void* b) {
    return (*(int*)b - *(int*)a);
}

int matchPlayersAndTrainers(int* players, int playersSize, int* trainers, int trainersSize) {
    qsort(players, playersSize, sizeof(int), compare_desc);
    qsort(trainers, trainersSize, sizeof(int), compare_desc);
    int i = 0;
    int j = 0;
    int answer = 0;
    while (true) {
        if (players[i] <= trainers[j]) {
            answer++;
            i++;
            j++;
        } else {
            i++;
        }
        if (i >= playersSize || j >= trainersSize) {
            break;
        }
    }
    return answer;
}