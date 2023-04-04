class Solution:
    def partitionString(self, s: str) -> int:
        result = 1
        char_dict = []
        
        for i in s:
            if i not in char_dict:
                char_dict.append(i)
            else:
                result += 1
                char_dict = [i]
        
        return result