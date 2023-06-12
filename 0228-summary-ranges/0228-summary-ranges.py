class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        stack = []
        result = []
        
        if len(nums) == 0:
            return []
        
        for i in nums:
            if len(stack) == 0:
                stack.append(i)
            else:
                if max(stack) + 1 == i:
                    stack.append(i)
                else:
                    if len(stack) == 1:
                        result.append(str(stack[0]))
                    else:
                        result.append(str(min(stack))+"->"+str(max(stack)))
                    stack.clear()
                    stack.append(i)
        
        if len(stack) == 1:
            result.append(str(stack[0]))
        else:
            result.append(str(min(stack))+"->"+str(max(stack)))
        
        return result
        