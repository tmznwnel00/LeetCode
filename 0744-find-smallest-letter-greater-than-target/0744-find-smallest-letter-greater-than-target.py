class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters_set = set(letters)
        start = ord(target) + 1
        while start <= 122:
            if chr(start) in letters_set:
                return chr(start)
            else:
                start += 1
        return letters[0]