# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.index = -1
        self.stack = []
        def flatten(nestedList):
            for i in nestedList:
                if i.isInteger():
                    self.stack.append(i.getInteger())
                else:
                    flatten(i.getList())
        
        self.flattened = flatten(nestedList)
        
        
    def next(self) -> int:
        self.index += 1
        return self.stack[self.index]
    
    def hasNext(self) -> bool:
        return True if self.index < len(self.stack) - 1 else False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())