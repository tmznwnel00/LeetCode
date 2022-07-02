class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        
        max_h = 0
        max_w = 0
        
        for i in range(len(horizontalCuts) - 1):
            if horizontalCuts[i + 1] - horizontalCuts[i] > max_h:
                max_h = horizontalCuts[i + 1] - horizontalCuts[i]
        
        for i in range(len(verticalCuts) - 1):
            if verticalCuts[i + 1] - verticalCuts[i] > max_w:
                max_w = verticalCuts[i + 1] - verticalCuts[i]
        return (max_h * max_w) % (10**9 + 7) 