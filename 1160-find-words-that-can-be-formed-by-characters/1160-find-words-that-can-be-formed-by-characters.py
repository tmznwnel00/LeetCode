from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        answer = 0
        for word in words:
            t = Counter(word)
            flag = 1
            for key, value in t.items():
                if key in c and c[key] >= value:
                    continue
                else:
                    flag = 0
                    break
            if flag:
                answer += len(word)
        return answer
            
        