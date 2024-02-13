class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            start, end = 0, len(word) - 1
            while start <= end:
                if word[start] != word[end]:
                    break
                else:
                    start += 1
                    end -= 1
            if start > end:
                return word
        return ""
            