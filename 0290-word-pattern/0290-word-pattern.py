class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        
        s_split = s.split()
        
        if len(s_split) != len(pattern):
            return False
        
        for index, key in enumerate(s_split):            
            if pattern[index] not in pattern_dict.keys():
                if key not in pattern_dict.values():
                    pattern_dict[pattern[index]] = key
                else:
                    return False
            else:
                if pattern_dict[pattern[index]] != key:
                    return False
                
        return True