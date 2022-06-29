class Solution(object):
    def kWeakestRows(self, mat, k):
        mat = list(map(sum, mat))
        answer = []
        max_val = max(mat)
        for i in range(k):
            index = mat.index(min(mat))
            answer.append(index)
            mat[index] = max_val + 1
        return answer
        
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        