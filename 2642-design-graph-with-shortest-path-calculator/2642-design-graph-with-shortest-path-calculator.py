from collections import defaultdict
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.outdegree = [defaultdict(dict) for i in range(n)]
        for i, j, weight in edges:
            self.outdegree[i][j] = weight
        
    def addEdge(self, edge: List[int]) -> None:
        self.outdegree[edge[0]][edge[1]] = edge[2]

    def shortestPath(self, node1: int, node2: int) -> int:
        visited = set([node1])
        weight = [None for i in range(len(self.outdegree))]
        for key, value in self.outdegree[node1].items():
            
            weight[key] = value
        weight[node1] = 0
        while True:
            min_index = -1
            min_val = float('inf')
            
            for i, w in enumerate(weight):
                if w is not None and w < min_val and i not in visited:
                    min_index = i
                    min_val = w
                    
            if min_index == -1:
                break
                
            visited.add(min_index)
            
            for key, value in self.outdegree[min_index].items():
                if (weight[key] is None) or (min_val + value < weight[key]):
                    weight[key] = min_val + value

        return weight[node2] if weight[node2] is not None else -1
        
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)