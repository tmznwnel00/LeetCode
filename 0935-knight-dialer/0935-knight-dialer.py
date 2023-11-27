class Solution:
    def knightDialer(self, n: int) -> int:
        hash_map = {1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[1,7,0], 7:[2,6], 8:[1,3], 9:[2,4], 0:[4,6]}
        x, y, z, c = 1, 1, 1, 1
        
        if n == 1:
            return 10
        for i in range(1, n):
            x, y, z, c = z+c, 2*z, y+2*x, 2*x
        return (4*x + 1*y + 2*z + 2*c) % (10**9+7)
                    