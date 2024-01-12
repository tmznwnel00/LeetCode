class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum(map(lambda c: s.lower()[:len(s)//2].count(c), ['a', 'e', 'i', 'o', 'u'])) == sum(map(lambda c: s.lower()[len(s)//2:].count(c), ['a', 'e', 'i', 'o', 'u']))