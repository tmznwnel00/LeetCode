class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        answer = []
        potions.sort()

        for spell in spells:
            threshold = math.ceil(success / spell)
            l = 0
            r = len(potions)
            while l < r:
                m = (l + r) // 2
                if potions[m] >= threshold and potions[m - 1] < threshold:
                    answer.append(len(potions) - m)
                    break
                elif potions[m] < threshold:
                    l = m + 1
                else:
                    r = m
            if l == r and potions[0] < threshold:
                answer.append(0)
            elif l == r and potions[0] >= threshold:
                answer.append(len(potions))
        
        return answer