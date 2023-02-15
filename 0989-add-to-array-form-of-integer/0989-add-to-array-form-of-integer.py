class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ''.join(map(str, num))
        a = int(s) + k
        answer = []
        for i in str(a):
            answer.append(int(i))
        return answer