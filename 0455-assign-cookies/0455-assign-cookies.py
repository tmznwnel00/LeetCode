class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        pointer = 0
        answer = 0
        for cookie in s:
            if pointer >= len(g):
                break
            if cookie >= g[pointer]:
                answer += 1
                pointer += 1
            else:
                continue
        return answer