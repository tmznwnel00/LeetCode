class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges = []
        vertexes = []
        
        for i, j in connections:
            i_index = -1
            j_index = -1
            
            for index, vertex in enumerate(vertexes):
                if i in vertex:
                    i_index = index
                if j in vertex:
                    j_index = index
                if i_index != -1 and j_index != -1:
                    break
            
            if i_index == -1 and j_index == -1:
                vertexes.append(set([i, j]))
                edges.append(1)
            elif i_index != -1 and j_index == -1:
                vertexes[i_index].add(j)
                edges[i_index] += 1
            elif i_index == -1 and j_index != -1:
                vertexes[j_index].add(i)
                edges[j_index] += 1
            elif i_index == j_index:
                edges[i_index] += 1
            else:
                min_val = min(i_index, j_index)
                max_val = max(i_index, j_index)
                vertexes[min_val] = vertexes[min_val].union(vertexes[max_val])
                edges[min_val] += edges[max_val]
                edges[min_val] += 1
                del vertexes[max_val]
                del edges[max_val]
        
        sum_vertex = 0
        leftover = 0
        for index, vertex in enumerate(vertexes):
            sum_vertex += len(vertex)
            leftover += edges[index] - (len(vertex) - 1)
        connection = n - sum_vertex
        connection += len(vertexes) - 1
        
        if leftover >= connection:
            return connection
        else:
            return -1
        
        
        
                    