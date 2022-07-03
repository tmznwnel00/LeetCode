class Solution(object):
    def decodeMessage(self, key, message):
        key = str(key)
        message = str(message)
        d = {}
        ascii = 97
        answer = ""
        d[' '] = ' '
        for i in range(len(key)):
            if len(d) == 27:
                break
            if key[i] == ' ':
                continue
            elif key[i] not in d:
                d[key[i]] = chr(ascii)
                ascii += 1
            else:
                continue
        for i in range(len(message)):
            answer = answer + d[message[i]]
        return answer