class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        temp = [x for x in letters if x > target]
        
        if len(temp) == 0:
            return sorted(letters)[0]
        else:
            return sorted(temp)[0]