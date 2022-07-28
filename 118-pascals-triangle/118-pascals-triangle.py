class Solution(object):
    def generate(self, numRows):
        answer = []
        for i in range(1, numRows + 1):
            tmp = []
            print(answer)
            for j in range(i):             
                if j == 0 or j == i - 1:
                    tmp.append(1)
                else:
                    tmp2 = answer[i - 2]
                    tmp.append(tmp2[j - 1] + tmp2[j])
            answer.append(tmp)
        return answer
        