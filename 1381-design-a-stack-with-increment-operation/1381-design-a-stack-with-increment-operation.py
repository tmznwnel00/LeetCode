class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.list = []

    def push(self, x: int) -> None:
        if len(self.list) < self.maxSize:
            self.list.append(x)

    def pop(self) -> int:
        if self.list:
            return self.list.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        m_k = min(k, len(self.list))
        for i in range(m_k):
            self.list[i] += val
        
            


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)