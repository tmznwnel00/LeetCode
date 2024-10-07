class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) >= len(sentence2):
            s1 = sentence1.split()
            s2 = sentence2.split()
        else:
            s1 = sentence2.split()
            s2 = sentence1.split()
            
        prefix, suffix = 0, 0
        
        while prefix < len(s2):
            if s1[prefix] == s2[prefix]:
                prefix += 1
            else:
                break
                
        while suffix < len(s2):
            if s1[-suffix-1] == s2[-suffix-1]:
                suffix += 1
            else:
                break
        
        if prefix + suffix < len(s2):
            return False
        else:
            return True
            