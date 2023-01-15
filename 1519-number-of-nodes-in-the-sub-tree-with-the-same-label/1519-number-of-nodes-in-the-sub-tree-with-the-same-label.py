from collections import deque, Counter
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        l_list = {i : {} for i in range(n)}
        answer = []
        num = 0
        for l in labels:
            d = {}
            d[l] = 1
            l_list[num] = d
            num += 1

        n_dict = {}
        node_list = {i : set([]) for i in range(n)} 

        for a, b in edges:
            node_list[a].add(b)
            node_list[b].add(a)
        q = set([])
        len_list = {i : 0 for i in range(n)}
        for i in range(len(node_list)):
            len_list[i] = len(node_list[i])
            if i != 0 and len(node_list[i]) == 1:
                q.add(i)
        for i in range(n-1):
            k = q.pop()
            root = node_list[k].pop()
            d1 = l_list[k]
            d2 = l_list[root]
            node_list[root].remove(k)
            len_list[root] -= 1
            if root not in q and root != 0 and len_list[root] == 1 :
                q.add(root)

            c1 = Counter(d1)
            c2 = Counter(d2)
            l_list[root] = dict(c1 + c2)
        for i in range(n):
            answer.append(l_list[i][labels[i]])
        return answer