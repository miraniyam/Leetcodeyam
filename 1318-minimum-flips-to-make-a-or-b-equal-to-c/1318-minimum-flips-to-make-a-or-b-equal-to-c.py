class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a2 = list(format(a, 'b'))
        b2 = list(format(b, 'b'))
        c2 = list(format(c, 'b'))
                
        maxLen = max(len(a2), len(b2), len(c2))
        
        # padding
        for i in range(maxLen-len(a2)):
            a2.insert(0, '0')
        for i in range(maxLen-len(b2)):
            b2.insert(0, '0')
        for i in range(maxLen-len(c2)):
            c2.insert(0, '0')
            
        print(a2, b2, c2)
        
        # fliping
        count = 0
        for i in range(maxLen):            
            if c2[i] == '0':
                if a2[i] != b2[i]:
                    count += 1
                else: # a2[i] == b2[i]
                    if a2[i] == '1':
                        count += 2
            else: # ci == '1'
                if a2[i] == b2[i]:
                    if a2[i] == '0':
                        count += 1    
        
        return count