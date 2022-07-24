class Solution(object):
    def searchMatrix(self, matrix, target):
        x = len(matrix)
        y = len(matrix[0])
        
        for i in range(x):
            if matrix[i][0] > target:
                break
            for j in range(y):
                if matrix[i][j] == target:
                    return True
                if matrix[i][j] > target:
                    break
            
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        zz