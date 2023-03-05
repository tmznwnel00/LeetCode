class Trie:

    def __init__(self):
        self.trie_set = set([])

    def insert(self, word: str) -> None:
        self.trie_set.add(word)

    def search(self, word: str) -> bool:
        if word in self.trie_set:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for s in self.trie_set:
            if s.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)