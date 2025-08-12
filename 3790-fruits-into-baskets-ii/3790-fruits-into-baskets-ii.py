class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        answer = 0
        for fruit in fruits:
            index = 0
            while True:
                if index == len(baskets):
                    answer += 1
                    break
                if baskets[index] >= fruit:
                    del baskets[index]
                    break
                else:
                    index += 1
                
        return answer

            