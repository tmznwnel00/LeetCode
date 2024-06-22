class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_value = sum(customers[:minutes]) - sum([i*(1-j) for i, j in zip(customers[:minutes], grumpy[:minutes])])
        
        max_index = 0
        now = sum(customers[:minutes])
        now_profit = max_value
        
        for i in range(len(customers) - minutes):
            now -= customers[i]
            now += customers[i+minutes]
            now_profit += grumpy[i+minutes] * customers[i+minutes]
            now_profit -= grumpy[i] * customers[i]
            if  now_profit  > max_value:
                max_value =  now_profit
                max_index = i + 1
        
        answer = sum([i*(1-j) for i, j in zip(customers[:max_index], grumpy[:max_index])])
        answer += sum(customers[max_index:max_index+minutes])
        answer += sum([i*(1-j) for i, j in zip(customers[max_index+minutes:], grumpy[max_index+minutes:])])
        
        
        return answer
                
            
            
                
            