class Solution(object):
    def fillCups(self, amount):
        answer = 0
        answer += max(amount)
        del amount[amount.index(max(amount))]
        print(amount)
        x = max(amount)
        y = min(amount)
        diff = x - y
        answer += max(0, y - ((answer - diff) // 2))

            
        return answer