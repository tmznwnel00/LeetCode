class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        nodes = set([i for i in range(n)])
        deletes = set([])
        
        for a, b in edges:
            deletes.add(b)
        
        return list(nodes - deletes)[0] if len(nodes - deletes) == 1 else -1
        
        