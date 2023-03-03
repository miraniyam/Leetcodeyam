class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) > 0:
            result = 1
        else:
            return 0
        for i in range(0, len(s)-1):
            d = [s[i]]
            tempCnt = 1
            for j in range(i+1, len(s)):
                if s[j] in d:
                    break
                else:
                    d.append(s[j])
                    tempCnt +=1
            if result < tempCnt:
                result = tempCnt
        
        return result