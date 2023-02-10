class Solution:
    def equalFrequency(self, word: str) -> bool:
        
        for i in range(0, len(word)):
            
            temp = word[:i] + word[i+1:]
            
            word_dict = {}

            for j in temp:
                if j in word_dict.keys():
                    word_dict[j] += 1
                else:
                    word_dict[j] = 1
            
            if min(word_dict.values()) == max(word_dict.values()):
                return True
        
        return False