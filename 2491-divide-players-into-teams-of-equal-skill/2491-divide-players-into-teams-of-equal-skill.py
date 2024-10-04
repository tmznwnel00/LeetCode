class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        val = skill[0] + skill[-1]
        answer = 0
        
        for i in range(len(skill)//2):
            if skill[i] + skill[-1*i -1] != val:
                return -1
            else:
                answer += skill[i] * skill[-1*i -1]
        return answer