class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        
        people.sort(reverse=True)
        
        left = 0
        right = len(people)-1
        
        while left <= right:
            if people[left] + people[right] > limit:
                left += 1
            else:
                left += 1
                right -= 1
            result += 1
        
        return result