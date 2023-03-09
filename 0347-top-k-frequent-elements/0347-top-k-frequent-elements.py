from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        l1 = []
        l2 = []
        for key, value in dict(counter).items():
            # print(key, value)
            check = 0
            for index, l_value in enumerate(l1):
                if l_value <= value:
                    check = 1
                    l1.insert(index, value)
                    l2.insert(index, key)
                    break
                    
            if check == 0:
                l1.append(value)
                l2.append(key)
        # print(l1, l2)
        return l2[:k]