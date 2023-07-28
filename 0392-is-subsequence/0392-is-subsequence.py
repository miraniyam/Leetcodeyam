class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = list(t)
        index = []
        
        for i in range(len(s)):
            if s[i] in t:
                if len(index) > 0:
                       if max(index) > t.index(s[i]):
                            return False
                index.append(t.index(s[i]))
                for j in range(t.index(s[i])+1):
                    t[j] = '1'
            else:
                return False
        
        return True