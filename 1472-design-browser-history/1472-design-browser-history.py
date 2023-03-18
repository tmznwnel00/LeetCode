class BrowserHistory:

    def __init__(self, homepage: str):
        self.l = [homepage]
        self.d = {homepage : 0}
        self.now = homepage
    def visit(self, url: str) -> None:
        index = self.d[self.now]
        self.l = self.l[:index + 1]
        self.now = url
        self.l.append(self.now)
        self.d[self.now] = index + 1
        # print(self.d)

    def back(self, steps: int) -> str:
        index = self.d[self.now]
        self.now = self.l[max(0, index - steps)]
        return self.l[max(0, index - steps)]

    def forward(self, steps: int) -> str:
        index = self.d[self.now]
        self.now = self.l[min(len(self.l) - 1, index + steps)]
        return self.l[min(len(self.l) - 1, index + steps)]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)