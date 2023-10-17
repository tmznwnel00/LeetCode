from collections import defaultdict
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents_dict = defaultdict(set)
        for i in range(n):
            if leftChild[i] in parents_dict or rightChild[i] in parents_dict:
                return False
            elif i in parents_dict and (leftChild[i] in parents_dict[i] or rightChild[i] in parents_dict[i]):
                return False
            else:
                if leftChild[i] != -1:
                    parents_dict[leftChild[i]].add(i)
                if rightChild[i] != -1:
                    parents_dict[rightChild[i]].add(i)
                if i in parents_dict:
                    if leftChild[i] != -1:
                        parents_dict[leftChild[i]] = parents_dict[leftChild[i]] | parents_dict[i]
                    if rightChild[i] != -1:
                        parents_dict[rightChild[i]] = parents_dict[rightChild[i]] | parents_dict[i]
        if n - len(parents_dict) >= 2:
            return False
            
        return True
                
                
            