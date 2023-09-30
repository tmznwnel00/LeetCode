class Solution:
    def candy(self, ratings: List[int]) -> int:
        left_list = [1] * len(ratings)
        
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i+1]:
                left_list[i+1] = left_list[i] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i] < ratings[i-1]:
                left_list[i-1] = max(left_list[i-1], left_list[i] + 1)
        
        return sum(left_list)
            