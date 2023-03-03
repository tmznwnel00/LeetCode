class Solution:
    def compress(self, chars: List[str]) -> int:
        s = chars[0]
        now = 1
        while True:
            if now == len(chars):
                break
            if chars[now] not in s:
                if len(s) > 1:
                    for i, j in enumerate(str(len(s))):
                        chars.insert(now + i, j)
                    now += len(str(len(s)))
                s = chars[now]
                now += 1
            else:
                s += chars[now]
                del chars[now]
        if len(s) > 1:
                for i, j in enumerate(str(len(s))):
                    chars.insert(now + i, j)
        return len(chars)
                