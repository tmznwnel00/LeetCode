class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set([])
        for index, value in enumerate(s):
            if value not in s[index+1:] and value not in visited:
                return index
            visited.add(value)
        return -1