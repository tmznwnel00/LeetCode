class SmallestInfiniteSet(object):

    def __init__(self):
        self.l = set()

    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.l) == 0:
            self.l.add(1)
            return 1
        else:
            now = 0
            while True:
                now += 1
                if now in self.l:
                    continue
                else:
                    self.l.add(now)
                    return now
                
        
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num in self.l:
            self.l.remove(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)